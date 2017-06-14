from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	DEPT_CHOICES = (
		('CSE', 'CSE'),
		('ECE', 'ECE'),
		('EEE', 'EEE'),
		('MECH', 'MECH'),
		('ICE', 'ICE'),
		('CHEM', 'CHEM'),
		('PROD', 'PROD'),
		('CIVIL', 'CIVIL'),
		('META', 'META'),
	)
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	resume_file = models.FileField(upload_to  = "/builder/")
	name = models.CharField(max_length = 200)
	address = models.TextField(max_length = 2000, default = "")
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	nationality = models.CharField(max_length = 2000, default = "")
	email_id = models.EmailField(max_length = 2000, default = "")
	dob = models.CharField(max_length = 1000, default = "")
	fname = models.CharField(max_length = 1000, default = "")
	languages = models.CharField(max_length = 1000, default = "")
	branch = models.CharField(max_length=5, choices=DEPT_CHOICES)
	cgpa = models.CharField(max_length = 1000, default = "")
	programming_languages = models.CharField(max_length = 1000, default = "")
	operating_systems = models.CharField(max_length = 1000, default = "")
	packages = models.CharField(max_length = 1000, default = "")
	acad_details = models.TextField(max_length = 10000, default = "")
	sports_details = models.TextField(max_length = 10000, default = "")
	other_details = models.TextField(max_length = 10000, default = "")
	pos_of_resp = models.TextField(max_length = 10000, default = "")
	xth_class_board = models.CharField(max_length = 1000, default = "")
	xth_class_marks = models.CharField(max_length = 10, default = "")
	xth_class_school = models.CharField(max_length = 1000, default = "")
	xth_class_year = models.CharField(max_length = 5, default = "")
	xiith_class_board = models.CharField(max_length = 1000, default = "")
	xiith_class_marks = models.CharField(max_length = 10, default = "")
	xiith_class_school = models.CharField(max_length = 1000, default = "")
	xiith_class_year = models.CharField(max_length = 5, default = "")

# class Project(models.Model):
# 	title = models.CharField(max_length = 200, blank=True,null=True)
# 	detail = models.TextField(blank=True,null=True)
# 	start_date = models.DateField(default = datetime.now(),blank=True,null=True)
# 	end_date = models.DateField(default = datetime.now(),blank=True,null=True)
# 	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

# Create your models here.
