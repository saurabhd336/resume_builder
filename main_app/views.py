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

def generate_file(resume, filename = None):
	try:
		file_generator = {"config.debug":True}
		file_generator["config.inputFile"] = "ugprefinal.docx"
		file_generator["config.outputFile"] = filename + ".docx"
		file_generator["config.debug"] = True
		file_generator["name_full"] = resume.name
		
		file_generator["address"] = []
		address_lines = resume.address.split('\n')
		for line in address_lines:
			temp = {"value" : line}
			file_generator["address"].append(temp)
		file_generator["gender"] = resume.gender
		file_generator["nationality"] = resume.nationality
		file_generator["email_id"] = resume.email_id
		file_generator["dob"] = str(resume.dob)
		file_generator["age"] = "19"
		file_generator["fname"] = resume.fname
		file_generator["langs"] = resume.languages
		file_generator["branch"] = resume.branch
		file_generator["cgpa"] = resume.cgpa
		file_generator["school_details"] = []
		
		v1 = {"class" : "X", "board" : resume.xth_class_board, "year" : resume.xth_class_year, 
				"school_name" : resume.xth_class_school, "marks" : resume.xth_class_marks}
		v2 = {"class" : "XII", "board" : resume.xiith_class_board, "year" : resume.xiith_class_year, 
				"school_name" : resume.xiith_class_school, "marks" : resume.xiith_class_marks}
		file_generator["school_details"].append(v1)
		file_generator["school_details"].append(v2)
		file_generator["academic_details"] = []
		
		acad_lines = resume.acad_details.split('\n')
		
		for line in acad_lines:
			v = {"value" : line}
			file_generator["academic_details"].append(v)
		file_generator["programming_langs"] = resume.programming_languages
		file_generator["operating_sys"] = resume.operating_systems
		file_generator["packages"] = resume.packages
		
		#Adding the projects
		
		file_generator["project_details"] = []
		# for f in formset:
		# 	form = f.save(commit = False)
		# 	temp = {"title" : form.title, "start_date" : str(form.start_date), "end_date" : str(form.end_date), "details" : form.detail}
		# 	file_generator["project_details"].append(temp)
		
		
		json_data = json.dumps(file_generator)
		f = open(filename + ".json", 'w')
		f.write(json_data)
		f.close()
		os.system("docxtemplater " + filename + ".json")
		return True
	except Exception, e:
		print e
		return False

def new_resume(request):
	success = False
	if request.user.is_authenticated:
		resume_form = ResumeForm()
		# formset = ProjectFormSet(instance=Resume())
		if request.method == "POST":
			resume_form = ResumeForm(request.POST)
			if resume_form.is_valid():
				resume = resume_form.save(commit = False)
				# formset = ProjectFormSet(request.POST,request.FILES)
				# if formset.is_valid():
				# 	formset.save(commit = False)
				resume.user = request.user
				success = generate_file(resume, request.user.username)
				print "Here"
    			if success:
    				print "Here"
    				resume.resume_file.name = request.user.username + ".docx"
    				resume.save()
    				return HttpResponse("Your resume was saved")
		return render(request, 'new_resume.html', {'form' : resume_form})
	return HttpResponse("Not valid")

def edit_resume(request):
	success = False
	if not request.user.is_authenticated:
		return HttpResponse("Please login to continue")
	if request.user.is_authenticated:
		resume = get_object_or_404(Resume, user = request.user)
		resume_form = ResumeForm(instance = resume)
		if request.method == "POST":
			resume_form = ResumeForm(request.POST, instance = resume)
			if resume_form.is_valid():
				resume.save()
				success = generate_file(resume, request.user.username)
    			if success:
    				print "Here"
    				resume.resume_file.name = request.user.username + ".docx"
    				resume.save()
    				return HttpResponse("Your resume was saved")
		return render(request, 'edit_resume.html', {'form': resume_form})
	return HttpResponse("Not valid")

def download_resume(request):
	if request.user.is_authenticated:
		resume = get_object_or_404(Resume, user = request.user)
		r_file = open(resume.resume_file.url)
		print r_file
		response = HttpResponse(r_file)
		response['Content-Disposition'] = "attachment; filename=" + resume.resume_file.name.split("/")[-1]
		return response
	return HttpResponse("Please login to download your resume")

def delete_resume(request):
	return HttpResponse("Yet to implement")