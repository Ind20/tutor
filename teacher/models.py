from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class userProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num       = models.CharField(max_length = 15)
    age             = models.IntegerField(null=True)
    profile_pic     = models.ImageField(default='assets/profile.png', upload_to='images/profile/', null='true', blank='true')
    @property
    def get_profile_pic(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
         return "images/assets/profile.png"

class contactus(models.Model):
    fullname        = models.CharField(max_length=35)
    phone_num       = models.CharField(max_length=15)
    email           = models.EmailField()
    message         = models.TextField(max_length=1000)


class tutor(models.Model):
    first_name                   = models.CharField(max_length=35)
    last_name                    = models.CharField(max_length=35)
    nick_name                    = models.CharField(max_length=35, null=True)
    email                        = models.EmailField(unique=True)
    mobile                       = models.CharField(max_length=15, unique=True)
    nip                          = models.CharField(max_length=35, null=True)
    echelon                      = models.CharField(max_length=35, null=True)
    dob                          = models.DateField()
    age                          = models.PositiveIntegerField()
    gender                       = models.CharField(max_length=10)
    address_line1                = models.CharField(max_length=35)
    address_line2                = models.CharField(max_length=35, null=True)
    city                         = models.CharField(max_length=35)
    province                     = models.CharField(max_length=35)
    country                      = CountryField()
    zip                          = models.PositiveIntegerField()
    high_school_name             = models.CharField(max_length=250)
    high_school_passing_year     = models.DateField()
    high_school_grade            = models.CharField(max_length=10)
    graduation_degree            = models.CharField(max_length=250)
    graduation_college           = models.CharField(max_length=250)
    graduation_passing_year      = models.DateField()
    graduation_grade             = models.CharField(max_length=10)
    postgraduation_degree        = models.CharField(max_length=250)
    postgraduation_college       = models.CharField(max_length=250)
    postgraduation_passing_year  = models.DateField(null=True)
    postgraduation_grade         = models.CharField(max_length=10, null=True)
    research_degree              = models.CharField(max_length=250, null=True)
    research_college             = models.CharField(max_length=250, null=True)
    research_passing_year        = models.DateField(null=True)
    research_grade               = models.CharField(max_length=10, null=True)
    other_qualification          = models.TextField(max_length=1000, null=True)
    current_position             = models.CharField(max_length=35, null=True)
    current_organisation         = models.CharField(max_length=250, null=True)
    years_of_experience          = models.PositiveIntegerField()
