from django import forms
from django.contrib.auth.models import User
from .models import contactus, userProfile, qualification, experience, tutor


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


class tutorForm(forms.ModelForm):
    class Meta:
        model   = tutor
        fields  = '__all__'
        widgets = {

            'first_name': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter first name'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter last name'}),
            'nick_name': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter nick name'}),
            'email': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter email'}),
            'mobile': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter mobile number'}),
            'nip': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your NIP'}),
            'echelon': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your echlon'}),
            'dob': forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}),
            'age': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your age (enter only positive number)'}),
            'gender': forms.TextInput(attrs={'class' : 'form-control form-control-sm mb-5', 'placeholder':' Enter gender'}),
            'address_line1': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter address line 1'}),
            'address_line2': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter address line 2'}),
            'city': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your city'}),
            'province': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your province'}),
            'zip': forms.TextInput(attrs={'class' : 'form-control form-control-sm mb-5', 'placeholder':' Enter your zip (enter only positive number)'}),
            'high_school_name': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter high school'}),
            'high_school_passing_year':forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}),
            'high_school_grade': forms.TextInput(attrs={'class' : 'form-control form-control-sm mb-5', 'placeholder':' Enter high school grade'}),
            'graduation_degree': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter graduation degree'}),
            'graduation_college': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter graduation college'}),
            'graduation_passing_year':forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}),
            'graduation_grade': forms.TextInput(attrs={'class' : 'form-control form-control-sm mb-5', 'placeholder':' Enter graduation grade'}),
            'postgraduation_degree': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter postgraduation degree'}),
            'postgraduation_college': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter postgraduation college'}),
            'postgraduation_passing_year':forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}),
            'postgraduation_grade': forms.TextInput(attrs={'class' : 'form-control form-control-sm mb-5', 'placeholder':' Enter post graduation grade'}),
            'research_degree': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter research degree'}),
            'research_college': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter research college name'}),
            'research_passing_year':forms.DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}),
            'research_grade': forms.TextInput(attrs={'class' : 'form-control form-control-sm mb-5', 'placeholder':' Enter research grade'}),
            'other_qualification': forms.Textarea(attrs={'class' : 'form-control', 'placeholder':' Enter your other qualification, college, passing year and grage'}),
            'current_position': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your current position'}),
            'current_organisation': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter current organisation'}),
            'years_of_experience': forms.TextInput(attrs={'class' : 'form-control form-control-sm', 'placeholder':' Enter your years of experience (enter only positive number)'})

        }