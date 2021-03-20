from django.urls import include, path
from . import views

urlpatterns = [
    path("register/",views.register),
    path("login/",views.login_view),
    path("logout/",views.logout_view),
    path("verify/<uuid:code>/",views.verify),
    path("verify/new/",views.verify_again),
    
]
