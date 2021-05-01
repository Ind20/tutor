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



class qualification(models.Model):
    course          = models.CharField(max_length=250)
    school          = models.CharField(max_length=250)
    grade           = models.CharField(max_length=10)
    year            = models.DateField(auto_now=False, null=True)
    user            = models.ForeignKey(User, related_name='qualifications', on_delete=models.CASCADE)


class experience(models.Model):
    organisation    = models.CharField(max_length=250)
    post            = models.CharField(max_length=250)
    from_date       = models.DateField(max_length=10)
    to_date         = models.DateField(auto_now=False, null=True)
    user            = models.ForeignKey(User, related_name='experiences', on_delete=models.CASCADE)

class teacher(models.Model):
    first_name                   = models.CharField(max_length=35)
    last_name                    = models.CharField(max_length=35)
    nick_name                    = models.CharField(max_length=35)
    email                        = models.EmailField(unique=True)
    mobile                       = models.CharField(max_length=15, unique=True)
    nip                          = models.CharField(max_length=35)
    echelon                      = models.CharField(max_length=35)
    dob                          = models.DateField(auto_now=False, null=True)
    age                          = models.PositiveIntegerField()
    gender                       = models.CharField(max_length=10)
    address_line1                = models.CharField(max_length=35)
    address_line2                = models.CharField(max_length=35)
    city                         = models.CharField(max_length=35)
    province                     = models.CharField(max_length=35)
    country                      = CountryField()
    zip                          = models.PositiveIntegerField()
    high_school_name             = models.CharField(max_length=250)
    high_school_passing_year     = models.DateField(auto_now=False, null=True)
    high_school_grade            = models.CharField(max_length=10)
    graduation_degree            = models.CharField(max_length=250)
    graduation_college           = models.CharField(max_length=250)
    graduation_passing_year      = models.DateField(auto_now=False, null=True)
    graduation_grade             = models.CharField(max_length=10)
    postgraduation_degree        = models.CharField(max_length=250)
    postgraduation_college       = models.CharField(max_length=250)
    postgraduation_passing_year  = models.DateField(auto_now=False, null=True)
    postgraduation_grade         = models.CharField(max_length=10)
    research_degree              = models.CharField(max_length=250)
    research_college             = models.CharField(max_length=250)
    research_passing_year        = models.DateField(auto_now=False, null=True)
    research_grade               = models.CharField(max_length=10)
    other_qualification          = models.TextField(max_length=1000)
    current_position             = models.CharField(max_length=35)
    current_organisation         = models.CharField(max_length=250)
    years_of_experience          = models.PositiveIntegerField()
