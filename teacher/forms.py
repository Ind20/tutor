from django import forms
from django.contrib.auth.models import User
from .models import contactus, userProfile, qualification, experience, teacher


class contactusForm(forms.ModelForm):
    class Meta:
        model   = contactus
        fields  = ["fullname", "phone_num", "email", "message"]
        widgets = {
            'fullname': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.NumberInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message': forms.Textarea(attrs={'class' : 'form-control'})
        }



class userProfileForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ['age', 'phone_num']
        widgets = {
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.TextInput(attrs={'class' : 'form-control'})
        }



class userProfileUpdateForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ['age', 'phone_num', 'profile_pic']
        widgets = {
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.TextInput(attrs={'class' : 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'style' : 'margin-top:15px'}),
        }



class userUpdateForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'})
        }



class qualificationForm(forms.ModelForm):
    class Meta:
        model   = qualification
        fields  = ['course', 'school', 'grade', 'year']
        widgets = {
            'course': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Degree/Deploma/Others'}),
            'school': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'College/University/Institue'}),
            'grade': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'CGGA/Percentage'}),
            'year': forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control', 'placeholder':'Passing Year (YYYY-MM-DD)'})
        }


class  experienceForm(forms.ModelForm):
    class Meta:
        model   =  experience
        fields  = ['organisation', 'post', 'from_date', 'to_date']
        widgets = {
            'organisation': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'College/University/Institue'}),
            'post': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Your post'}),
            'from_date': forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control', 'placeholder':'From date(YYYY-MM-DD)'}),
            'to_date': forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control', 'placeholder':'To date (YYYY-MM-DD)'})
        }


class teacherForm(forms.ModelForm):
    class Meta:
        model   = teacher
        fields  = '__all__'
        widgets = {
        'first_name': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter first name'})
        }