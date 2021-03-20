from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from dashboard.models import Profile,Messages
from .models import Jobs,Qualification
from jobs.models import Applicant
from django.contrib.auth.models import User
import requests
# Create your views here.
def index(request):
    profile=Profile.objects.filter(user_id=request.user.id)
    profile=profile[len(profile)-1]
    return render(request,"employer/index.html",{
        "name":profile.name,


    })
def post_job(request):
    if request.method=="POST":
        title=request.POST["jobtitle"]
        jobdescription=request.POST["jobdescription"]
        qualification=request.POST["qualification"]
        salary=request.POST["salary"]
        mode=request.POST["mode"]

        profile=Profile.objects.filter(user_id=request.user.id)
        profile=profile[len(profile)-1]
        Jobs.objects.create(title=title,jobdescription=jobdescription,salary=salary,mode=mode,profile=profile.id).save()
        job=Jobs.objects.all()[::-1][0]
        
        qualify=qualification.split(",")
        for degree in qualify:
            Qualification(job_id=job.id,name=degree).save() 
        return HttpResponseRedirect(f"/jobs/{job.slug}")
    else:
        return render(request,'employer/new_post.html')


def all_applicants(request):
    unread_applications=[]
    profile=Profile.objects.get(user_id=request.user.id)
    jobs=Jobs.objects.filter(profile=profile.id)
    for job in jobs:
        app=Applicant.objects.filter(status=0 , job_id=job.id)
        name=Profile.objects.get(id=app.applicant_id)
        email=User.objects.get(id=app.applicant_id)    
        unread_applications.append([name,email,job.title,app.id])
        return render(request,"employer/applications.html",
        {
            "unread":unread_applications    
        })
def view_application(request,id):
    applicant=Applicant.objects.filter(id=id)
    job=Jobs.objects.get(id=applicant.job_id)
    user=User.objects.get(id=applicant.applicant_id)
    profile=Profile.objects.get(user_id=user.id)
    return render(request,"employer/application.html",{
        "applicant":applicant,
        "job":job,
        "user":user,
        "profile":profile
    })
def chat_with_applicant(request,applicants_id):
    if request.method=="POST":
        message=request.POST.get("message")
        recievers_id=Applicant.objects.get(id=applicants_id).applicant_id
        Messages(sender_id=request.user.id,reciever_id=recievers_id,application_id=applicants_id,message=message).save()
        return HttpResponseRedirect(f"employer/chat/{applicants_id}")

    else:
        applicant=Applicant.objects.get(id=applicants_id)
        job=Jobs.objects.get(id=applicant.job_id)
        message=Messages.objects.filter(application_id=applicants_id)
        profile=Profile.objects.get(user_id=applicant.applicant_id)
        profile1=Profile.objects.get(user_id=request.user.id)
        return render(request,"employer/conv.html",
        {
            "messages":message,
            "profile":profile,
            "job":job,
            "profile1":profile1
        })
def schedule_interview(request):
    if request.method=="POST":
        candidate=User.objects.get(id=(int(request.POST["candidate"])))
        candidate_profile=Profile.objects.get(user_id=candidate.id)
        application=Applicant.objects.get(applicant_id=candidate.id,job_id=int(request.POST["job"]))

        data=requests.post("https://api.zoom.us/v2/users/me/meetings",headers={
            'content-type':"application/json",
            "authorization":f"Bearer {request.session['zoom_access_token']}",
            
        }, data=json.dumps({
            "topic":f"Interview with {candidate_profile.name}",
            "type":2,
            "start_time":request.POST["time"],
        }))
        print(data.json()["join_url"],data.json()["start_url"])
        Messages(sender_id=request.user.id,reciever_id=candidate.id,application_id=application.id,message=f"You have been invited for an interview . Join this meeting <a href='{data.json()['join_url']}'>Enter Meeting </a> at {data.json()['start_time']} UTC").save()
        Messages(sender_id=request.user.id,reciever_id=candidate.id,application_id=application.id,message=f"To start the meeting click on link . Join this meeting <a href='{data.json()['start_url']}'>Enter Meeting </a> ",public=False).save()

        return HttpResponseRedirect(f"/employer/chat/{application.id}")

    else:
        profile=Profile.objects.get(user_id=request.user.id)
        jobs=Jobs.objects.filter(profile=profile.id)
        return render(request,"employer/interview.html",{
            "jobs":jobs,
        })