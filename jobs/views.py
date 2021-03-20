from django.shortcuts import render,HttpResponse
from employer.models import Jobs,Qualification
from dashboard.models import Profile
from .models import Applicant
# Create your views here.
def job_desc(request,code):
    job=Jobs.objects.get(slug=code)
    company=Profile.objects.get(id=job.profile).name
    qualification=Qualification.objects.get(job_id=job.id)
    print(qualification)
   
    return render(request,"job/job.html",{
        "job":job,
        "qualification":qualification ,
        "company":company   
    })
def apply_job(request,code):
    try:
        applied=Applicant.objects.get(applicant_id=request.user.id,job_id=Jobs.objects.get(slug=code).id)
    
        
        return render(request,"job/applied.html",
        {
            "message":"Already applied",
            "applicant":applied
        })
    except Applicant.DoesNotExist:
        pass
    if request.method=="POST":
        applicant_id=request.user.id
        job_id=Jobs.objects.get(slug=code).id
        resume=request.FILES['resume']
        experiences=request.POST["experiences"]
        expectations=request.POST["expectations"]
        cover=request.POST["cover"]
        Applicant(applicant_id=applicant_id,job_id=job_id,resume=resume,experiences=experiences,expectations=expectations,cover=cover).save()
        return render(request,"job/applied.html",{
            "message":"Applied Successfully"
        })
   
    else:
        job=Jobs.objects.get(slug=code)
        company=Profile.objects.get(id=job.profile).name
        profile=Profile.objects.get(id=request.user.id)
        return render(request,"job/apply.html",{
            "job":job,
            "company":company,
            "profile":profile,
        })
 
