from django.shortcuts import render, HttpResponseRedirect, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForms, NewProfile, AdminProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# if we are not using custom form otherwise use form file
# def sign_up(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             messages.success(request, 'user signup successfully')
#             fm.save()
#     else:
#         fm = UserCreationForm()
#     return render(request, 'app1/index.html', {'form': fm})


def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForms(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'user signup successfully')
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'app1/index.html', {'form': fm})
    else:
        fm = SignUpForms()
    return render(request, 'app1/index.html', {'form': fm})


def loginform(request):
    # if not request.user.is_authenticated():
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                return render(request, 'app1/login.html', {'form': fm})
    else:
        fm = AuthenticationForm()
    return render(request, 'app1/login.html', {'form': fm})
    # else:
    #     return HttpResponseRedirect("/profile/")


def user_profile(request):
    # if request.user.is_authenticated():
    if request.method == "POST":
        if request.user.is_superuser:
            fm = AdminProfile(request.POST, instance=request.user)
            users = User.objects.all()
        else:
            fm = NewProfile(request.POST, instance=request.user)
            users = None
        if fm.is_valid():
            fm.save()
            return render(request, 'app1/profile.html', {'form': fm, 'users': users})
    else:
        if request.user.is_superuser:
            fm = AdminProfile(instance=request.user)
            users = User.objects.all()
        else:
            fm = NewProfile(instance=request.user)
            users = None
        return render(request, 'app1/profile.html', {'form': fm, 'name': 'request.user', 'users': users})
        # else:
    #     return redirect('login/')


def user_logout(request):
    logout(request)
    return redirect('/login/')


def pass_change(request):
    # if request.user.is_authenticated():
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'app1/password.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
