from django.db import models
from django.contrib.auth.models import User
import uuid


PUBLIC_DNA_CHOICES = (('23andMe','23andMe'),
					('Ancestry','Ancestry'),
					('VeritasGenomics','Veritas Genomics'),
					('CompleteGenomics','Complete Genomics'),
					('FTDNA', 'Family Tree DNA'))

SELF_IDENTIFIED_CHOICES = (('African', 'African'),
						('Ad Mixed American', 'Ad Mixed American'),
						('East Asian', 'East Asian'),
						('European', 'European'),
						('South Asian', 'South Asian'),)

# Create your models here.
class PRS(models.Model):
	uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	user = models.ForeignKey(User, related_name = 'prs', on_delete=models.CASCADE)
	home_dir = models.CharField(max_length = 512)
	dna_source = models.CharField(max_length = 32, choices = PUBLIC_DNA_CHOICES)
	internal_usage_permission = models.BooleanField(default = False)
	self_identified_ancestry = models.CharField(max_length = 32, choices = SELF_IDENTIFIED_CHOICES)
	job_status = models.BooleanField(default = False)
	creation_date = models.DateField(auto_now_add = True , blank = True)

	def __str__(self):
		return (str(self.user.email) + " with ID: " + str(self.uuid))

