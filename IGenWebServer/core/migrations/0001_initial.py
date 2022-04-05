# Generated by Django 3.1.2 on 2020-11-22 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PRS',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('home_dir', models.CharField(max_length=512)),
                ('dna_source', models.CharField(choices=[('23andMe', '23andMe'), ('Ancestry', 'Ancestry'), ('Veritas Genomics', 'Veritas Genomics'), ('Complete Genomics', 'Complete Genomics')], max_length=32)),
                ('internal_usage_permission', models.BooleanField(default=False)),
                ('self_identified_ancestry', models.CharField(choices=[('African', 'African'), ('Ad Mixed American', 'Ad Mixed American'), ('East Asian', 'East Asian'), ('European', 'European'), ('South Asian', 'South Asian')], max_length=32)),
                ('job_status', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]