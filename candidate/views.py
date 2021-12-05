from django.shortcuts import render , redirect
from django.http import HttpResponse
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import job
from recruiter.models import application
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def job_page(request,jid):
    current_job = job.objects.filter(id=jid)
    request.session['jid']=jid
    return render(request,'job-page.html',{'job' : current_job[0]})

def browse_jobs(request):
    jobs = job.objects.all()
    return render(request,'browse-jobs.html',{'jobs':jobs})

def apply(request):
    if request.method=='POST':
        jid=request.session['jid']
        resume = request.FILES['resume']
        current_job = job.objects.filter(id=jid)
        job_description = current_job[0].description
        resume = docx2txt.process(resume)    
        #list of text to store resume and job description
        text = [job_description,resume]
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)
        print(count_matrix)
        match = cosine_similarity(count_matrix)[0][1]
        match = match*100
        match = round(match,2)
        current_job = job.objects.filter(id=jid)
        current_user=request.user
        current_application = application(user_id=current_user,job_id=current_job[0],resume=request.FILES['resume'],match=match)
        current_application.save()
        messages.info(request,match)
        return redirect("browse_jobs")
    else:
        return render(request,"apply.html")

    