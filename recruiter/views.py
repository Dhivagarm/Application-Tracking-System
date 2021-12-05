from django.shortcuts import render,redirect
from candidate.models import job
from recruiter.models import application
from django.contrib.auth.models import User

# Create your views here.

def add_job(request):
    if request.method=='GET':
        return render(request,"add-job.html")
    else:
        job_title = request.POST['title']
        job_description = request.POST['description']
        job_type = request.POST['type']
        print(job_description,job_title,job_type)
        current_user = request.user
        current_job = job(title=job_title,description=job_description,type=job_type,posted_by=current_user)
        current_job.save()
        return redirect("home")

def manage_applications(request):
    if request.method=='GET':
        user_id = request.user.id
        jobb = job.objects.filter(posted_by=user_id)
        applications=[]
        users=[]
        jobs=[]
        for jb in jobb:
            app = application.objects.filter(job_id=jb.id)
            for appl in app:
                applications.append(appl)
                users.append(User.objects.filter(id=appl.user_id.id)[0])
                jobs.append(job.objects.filter(id=appl.job_id.id)[0])
        requirements=[]
        for i in range(len(jobs)):
            c_dict = {
                'applicant_name' : users[i].username,
                'job_title' : jobs[i].title,
                'resume' : applications[i].resume.url,
                'match' : applications[i].match
            }
            requirements.append(c_dict)
        return render(request,"manage-applications.html",{'requirements' : requirements })   

        