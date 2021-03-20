from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.index),
    path("post",views.post_job),
    path("applicants/",views.all_applicants),
    path("applicants/<str:id>",views.view_application),
    path("chat/<str:id>",views.chat_with_applicant),
    path("schedule-interview/",views.schedule_interview),
    
]
