from django.conf.urls import url
from django.urls import path, re_path, include
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('contactus', views.contactus, name='contactus'),
    
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),

    path('addqualification', views.addqualification, name="addqualification"),
    path('editqualification/<int:id>', views.editqualification, name="editqualification"),
    path('addexperience', views.addexperience, name="addexperience"),
    path('editexperience/<int:id>', views.editexperience, name="editexperience"),


    path('dashboard', views.dashboard, name="dashboard"),
]