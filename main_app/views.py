from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from models import Resume
from .forms import ResumeForm
import json
import os

def index(request):
	return render(request, 'index.html')


def signin(request):
	if request.method == "POST":
		roll_no = request.POST.get("roll_no")
		password = request.POST.get("pass")
		user = authenticate(username = roll_no, password = password)
		if user != None:
			login(request, user)
			return render(request, 'success.html')
		else:
			return render(request, 'signin.html', 
				{'error' : "Invalid credentials or webmail is down. Please try again."})
	return render(request, 'signin.html')

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponse("You are logged out")

def about(request):
	return render(request, 'about.html')

def my_resume(request):
	if request.user.is_authenticated:
		resume = Resume.objects.filter(user = request.user)
		print resume
		if len(resume) != 0:
			result = {'status' : True, 'resume' : resume[0]}
		else:
			result = {'status' : False}
		return render(request, 'my_resume.html', {'r' : result})
	return HttpResponse("Not valid")

def new_resume(request):
	if request.user.is_authenticated:
		resume_form = ResumeForm()
		if request.method == "POST":
			resume_form = ResumeForm(request.POST)
			if resume_form.is_valid():
				resume = resume_form.save(commit = False);
				resume.user = request.user
				file_generator = {
     								"config.debug":True
     								}
    			file_generator["config.inputFile"] = "ugprefinal.docx"
    			file_generator["config.outputFile"] = request.user.username + ".docx"
    			file_generator["config.debug"] = True
    			file_generator["name_full"] = resume.name
    			file_generator["address"] = resume.address
    			file_generator["gender"] = resume.gender
    			file_generator["nationality"] = resume.nationality
    			file_generator["email_id"] = resume.email_id
    			file_generator["dob"] = str(resume.dob)

    			json_data = json.dumps(file_generator);

    			os.chdir("builder")
    			f = open(request.user.username + ".json", 'w')
    			f.write(json_data)
    			f.close()
    			os.system("docxtemplater " + request.user.username + ".json")
    			resume.resume_file.name = os.getcwd() + "/" + request.user.username + ".docx"
    			print resume.resume_file.name 
    			os.chdir("..")
    			resume.save()
    			return HttpResponse("Your resume was saved")
		return render(request, 'new_resume.html', {'form' : resume_form})
	return HttpResponse("Not valid")

def edit_resume(request):
	if request.user.is_authenticated:
		resume = get_object_or_404(Resume, user = request.user)
		resume_form = ResumeForm(instance = resume)
		if request.method == "POST":
			resume_form = ResumeForm(request.POST, instance = resume)
			if resume_form.is_valid():
				resume.save()
				return HttpResponse("Your resume was edited successfully")
		return render(request, 'edit_resume.html', {'form': resume_form})
	return HttpResponse("Not valid")

def download_resume(request):
	resume = Resume.objects.filter(user = request.user)
	if len(resume) != 0:
		r = resume[0]
		r_file = open(r.resume_file.url)
		print r_file
		response = HttpResponse(r_file)
		response['Content-Disposition'] = "attachment; filename=" + r.resume_file.name.split("/")[-1]
		return response
	return HttpResponse("Can't find your resume")

def delete_resume(request):
	return HttpResponse("Yet to implement")