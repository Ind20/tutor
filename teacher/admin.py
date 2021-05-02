from django.contrib import admin
from .models import contactus, userProfile, qualification, experience, tutor

class contactusAdmin(admin.ModelAdmin):
    list_display =('fullname', 'phone_num', 'email', 'message')

admin.site.register(contactus, contactusAdmin)


class userProfileAdmin(admin.ModelAdmin):
    list_display =('phone_num', 'age')

admin.site.register(userProfile, userProfileAdmin)

class qualificationAdmin(admin.ModelAdmin):
    list_display =('course', 'school', 'grade', 'year')

admin.site.register(qualification, qualificationAdmin)


class experienceAdmin(admin.ModelAdmin):
    list_display =('organisation', 'post', 'from_date', 'to_date')

admin.site.register(experience, experienceAdmin)

class tutorAdmin(admin.ModelAdmin):
    list_display =('first_name', 'last_name')

admin.site.register(tutor, tutorAdmin)