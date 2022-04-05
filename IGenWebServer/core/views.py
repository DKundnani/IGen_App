from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
import os
from .models import PRS, PUBLIC_DNA_CHOICES, SELF_IDENTIFIED_CHOICES
from IGenWebServer.settings import BASE_DIR
import threading
import logging
from .igen_supreme_manager import supreme_manager

# Create your views here.
def home(request):
	return render(request, 'homepage.html')

def about(request):
	return render(request, 'about.html')

def howitworks(request):
	return render(request, 'how.html')

def resources(request):
	return render(request, 'resources.html')

def docs(request):
	return render(request, 'signup.html')


def signup(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	elif request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		reenter_password = request.POST['reenter-password']
		username = email.split('@')[0]
		if password != reenter_password:
			return render(request, 'signup.html', {'error': "Passwords do not match."})

		#Check if the username already exists.
		if_usernames = User.objects.filter(email = email).count()
		if if_usernames != 0:
			return render(request, 'signup.html', {'error': "Please choose a different email. This email exists."})

		#Create User object and authenticate.
		user = User.objects.create_user(email = email, username = username, password = password)
		user = authenticate(request, username=username, password=password)

		#Log in the user.
		if user is not None:
			auth_login(request, user)
			return redirect('dashboard', permanent = True)


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	elif request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		username = email.split('@')[0]
		user = authenticate(request, username=username, password=password)

		#Log in the user.
		if user is not None:
			auth_login(request, user)
			return redirect('dashboard', permanent = True)
		else:
			return render(request, 'login.html', {'error': 'Password does not match'})

def logout(request):
	auth_logout(request)
	return render(request, 'homepage.html')


@login_required(login_url='/login/')
def dashboard(request, redirect_kwargs = None):
	if request.method == 'GET':
		if redirect_kwargs == None:
			user = request.user
			prs_files = user.prs.all()
			content = dict()
			content['prs'] = prs_files
			return render(request, 'dashboard.html', content)
		else:
			if "error" in redirect_kwargs:
				return render(request, 'dashboard.html', redirect_kwargs)


@login_required(login_url='/login/')
def upload_dna(request):
	if request.method == 'POST':
		user = request.user
		dna_source = "Ancestry"
		
		#Special case: FTDNA
		if dna_source == 'Family Tree DNA':
			dna_source = "FTDNA"

		internal_usage_permission = request.POST['auth']
		file = request.FILES['dna-file']
		self_identified_ancestry = request.POST['self-identified-ancestry']
		eng_to_bool = {'Yes': True, 'No': False}
		if internal_usage_permission not in eng_to_bool or dna_source not in [i[0] for i in PUBLIC_DNA_CHOICES] or self_identified_ancestry not in [i[0] for i in SELF_IDENTIFIED_CHOICES]: 
			return redirect('dashboard', {'error': 'Form fields are incorrect.'} , permanent = True)
		home_dir = os.path.join(BASE_DIR, "data", user.username)

		model_object_prs = PRS(user = user, 
								home_dir = home_dir, 
								dna_source = dna_source, 
								internal_usage_permission = eng_to_bool[internal_usage_permission], 
								self_identified_ancestry = self_identified_ancestry)

		#Save the file.
		file_dir = os.path.join(home_dir, str(model_object_prs.uuid))
		os.makedirs(file_dir)

		user_vcf_file_path = os.path.join(file_dir, 'inputfile')
		with open(user_vcf_file_path, "wb") as f:
			f.write(file.read())

		model_object_prs.save()

		#Arguments for the pipeline.
		arguments = {'prs_object':model_object_prs, 'user_home_dir':home_dir, 'user_vcf_file_path': user_vcf_file_path, 'dna_service_provider': dna_source}

		#Starting pipeline in the background.
		pipeline_thread = threading.Thread(target=run_pipeline, kwargs=arguments)
		pipeline_thread.start()

		return redirect('dashboard')
	elif request.method == 'GET':
		return redirect('dashboard',  permanent = True)


@login_required(login_url='/login/')
def check_status(request):
	user = request.user
	completed_prs = user.prs.all()

	#Read the Log files.
	content = dict()
	for prs_obj in completed_prs:
		prs_obj_home_dir = prs_obj.home_dir
		prs_obj_uuid = str(prs_obj.uuid)

		#Get the log file.
		prs_obj_log_file = os.path.join(prs_obj_home_dir, prs_obj_uuid, "pipeline.log")

		if not os.path.exists(prs_obj_log_file):
			continue
		#Read the log file.
		with open(prs_obj_log_file) as f:
			raw = f.read()

		status_entries = raw.split("\n")
		content[prs_obj_uuid] = status_entries
		#print(content)
	return render(request, 'status.html', {'content': content})


@login_required(login_url='/login/')
def show_results(request):
	user = request.user
	#Get the result file.
	completed_prs = user.prs.all().filter(job_status = True)
	content = dict()
	content['user'] = user
	content['prs'] = {'info':completed_prs[0]}

	#Read scores.
	with open(os.path.join(content['prs']['info'].home_dir, str(content['prs']['info'].uuid), "finaloutput", 'percentiles.txt')) as f:
		raw = f.read()

	content['prs']['scores'] = {i.split('\t')[0]:(int(i.split('\t')[1])) for i in raw.split('\n') if i != ''}
	
	return render(request, 'results.html', content)


def run_pipeline(prs_object, user_home_dir, user_vcf_file_path, dna_service_provider):
	log_file_path = os.path.join(user_home_dir, str(prs_object.uuid), "pipeline.log")
	logging.basicConfig(filename=log_file_path, filemode='w', format='[%(levelname)s] - %(message)s', level=logging.INFO)
	logging.info('Running Supreme Pipeline for: %s and PRS Object ID: %s', prs_object.user.email, str(prs_object.uuid))

	status = supreme_manager(os.path.join(user_home_dir, str(prs_object.uuid)), user_vcf_file_path, dna_service_provider)

	prs_object.job_status = True
	prs_object.save()
	return True

	'''
	2. Convert to VCF file. [Sara]
	3. Imputation and Phasing. [Sara]
	4. One Time - PCA [Saving]
	5. PRS []
	6. Percentile Calculations.
		Output Expectation:
			 HIV - 45%
			 Hep-B - 55%
			 Chicken Pox - 65%
	7. Generate Graphs.
	'''
