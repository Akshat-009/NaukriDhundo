from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("<str:code>/",views.job_desc),
    path("<str:code>/apply",views.apply_job),
]
