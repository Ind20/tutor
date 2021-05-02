from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import userProfile, tutor
from .forms import contactusForm, userProfileForm, userUpdateForm, userProfileUpdateForm, tutorForm, tutordetailForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'home.html')


def contactus(request):
    form = contactusForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Form submitted successfully')
        return redirect('contactus')
    else:
        return render(request, 'contactus.html', {'form': form})


def please_login(request):
    msg = "You need to be logged-in to view this page"
    messages.info(request, msg)
    return render(request, 'login.html')


def login(request):
    if request.user.is_authenticated:
        messages.info(request,'You are alredy logged in.')
        return redirect('profile')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request,'You are successfully logged in.')
                return redirect('/')
            else:
                messages.info(request,"Invalid username/password")
                return redirect('login')
        else:
            return render(request,"login.html")


def register(request):
    if request.user.is_authenticated:
        messages.info(request,'You are alredy registered.')
        return redirect('profile')
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_num = request.POST['phone_num']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is not available')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is alreday registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,
                                      email=email, first_name=first_name, last_name=last_name)
                user.save()
                newuserProfile = userProfile(phone_num=phone_num, user=user)
                newuserProfile.save()
                messages.info(request,'Account created successfully.')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    else:
        return render(request,"register.html")


@login_required
def profile (request):
    p_form          = userProfileForm(instance=request.user.userprofile)
    context = {
        'proj': p_form
    }
    return render(request, 'profile.html', context)


@login_required
def editprofile(request):
    if request.method =='POST':
        u_form = userUpdateForm(request.POST or None, instance=request.user)
        p_form = userProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.info(request,'Your profile successfully saved.')
        return redirect('profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = userProfileUpdateForm(instance=request.user.userprofile)
        return render(request, 'editprofile.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def apply(request):
    form = tutorForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
           form.save()
        messages.info(request,'Applied for tutor successfully')
        return redirect('/') 
    else:
        return render(request, 'apply.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request,'You are successfully logged out.')
    return redirect('login')



@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def dlogin(request):
    if request.user.is_authenticated:
        messages.info(request,'You are alredy logged in.')
        return redirect('dashboard')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard')
            else:
                messages.info(request,"Invalid username/password")
                return redirect('dlogin')
        else:
            return render(request,"dashboard/login.html")

@login_required
def dlogout(request):
    auth.logout(request)
    return redirect('/dashboard/login')


@login_required
def upload(request):
    return render(request, 'dashboard/upload.html')

@login_required
def addtutor(request):
    form = tutorForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
           form.save()
        messages.info(request,'Tutor added successfully')
        return redirect('/dashboard/tutorlist') 
    else:
        return render(request, 'dashboard/addtutor.html', {'form': form})

@login_required
def tutorlist(request):
    tutors     = tutor.objects.all()
    return render(request, 'dashboard/tutorlist.html', {'tutors': tutors})


@login_required
def tutordetail(request, id):
    tutordetails = tutor.objects.get(id=id)
    form = tutordetailForm(request.POST or None, instance=tutordetails)
    return render(request, 'dashboard/tutordetails.html', {'form': form, 'tutordetails': tutordetails})


@login_required
def edittutor(request, id):
    tutordetails = tutor.objects.get(id=id)
    form = tutorForm(request.POST or None, instance=tutordetails)
    if request.method=='POST':
        if form.is_valid():
           form.save()
        messages.info(request,'Tutor details updated successfully')
        return redirect('/dashboard/tutor/%s' %id) 
    else:
        return render(request, 'dashboard/edittutor.html', {'form': form, 'tutordetails': tutordetails})


@login_required
def result(request):
    return render(request, 'dashboard/result.html')