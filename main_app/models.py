from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	resume_file = models.FileField(upload_to  = "/builder/")
	name = models.CharField(max_length = 200)
	address = models.CharField(max_length = 2000, default = "")
	gender = models.CharField(max_length = 2000, default = "")
	nationality = models.CharField(max_length = 2000, default = "/")
	email_id = models.EmailField(max_length = 2000, default = "")
	dob = models.DateField(default = datetime.now())
# Create your models here.
