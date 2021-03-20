from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from jobs.models import Applicant
from .models import Messages
from employer.models import Jobs,Qualification
from django.http import HttpResponseRedirect,HttpResponse
import requests
import base64
# Create your views here.



def base64_encode(message):
    message_bytes=message.encode("ascii")
    base64_bytes=base64.b64encode(message_bytes)
    base64_message=base64_bytes.decode("ascii")
    return base64_message
@login_required(login_url="/auth/login/")
def index(request):
    if request.session.get("role") is None:
        try:
            Profile.objects.get(user_id=request.user.id)[0]
        except Profile.DoesNotExist:
            
             return HttpResponseRedirect("/register-first")
    elif int (request.session.get("role")==0):
        return HttpResponseRedirect("/employer")
    return HttpResponseRedirect("dashboard")
@login_required(login_url="/auth/login")
def register_first(request):
    if request.method=="POST":
        role=int(request.POST['role'])
        name=request.POST.get("username")
        Profile(user_id=request.user.id,role=role,name=name).save()
        request.session["role"]=int(request.POST['role'])
        return HttpResponseRedirect("/")
    else:
        return render(request,"dash/register-first.html")
@login_required(login_url="/auth/login")
def chat_with_applicant(request,applicants_id):
    if request.method=="POST":
        message=request.POST.get("message")
        recievers_id=Applicant.objects.get(id=applicants_id).applicant_id
        Messages(sender_id=request.user.id,reciever_id=recievers_id,application_id=applicants_id,message=message).save()
        return HttpResponseRedirect(f"/chat/{applicants_id}")

    else:
        applicant=Applicant.objects.get(id=applicants_id)
        job=Jobs.objects.get(id=applicant.job_id)
        message=Messages.objects.filter(application_id=applicants_id)
        profile=Profile.objects.get(user_id=applicant.applicant_id)
        profile1=Profile.objects.get(id=job.profile)
        return render(request,"dashboard/conv.html",
        {
            "messages":message,
            "profile":profile,
            "job":job,
            "profile1":profile1
        })

def zoom_interview(request):
    code=request.GET["code"]
    data=requests.post(f"https://zoom.us/oauth/token?grant_type=authorization_code&code={code}&redirect_uri=http://127.0.0.1:8000/interview/callback",header={
    "Authorization":f"Basic {base64_encode('3PjxsoRUTsaaP3sQJpJ7PQ:R4wslcm4Kquh40gaQVzB2VE94WX66bYC')}"
})
    request.session["zoom_access_token"]=data.json()["access_token"]
    #print(data)
    return HttpResponseRedirect("/employer/schedule-interview")


def search_job(request):
    query= request.GET["query"]
    if query:
        jobs=Jobs.objects.filter(title__contains=query)
        if request.GET.get("page"):
            page=int(request.GET["page"])
            if page==1:
                jobs=Jobs.objects.filter(title__contains=query)[0:4]
            else:
                jobs=Jobs.objects.filter(title__contains=query)[4*(p-1):4*p]
        return render(request,"dash/results.html",{
            "jobs":jobs,
            "pagination":[job+1 for job in range(math.ceil(len(jobs)/4))],
            "current":"".join([None if request.GET.get("page")==None else request.GET.get("page")]),
            "query":request.GET["query"]
        })
    else:
        return render(request,"dash/index.html")
    
