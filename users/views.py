from django.shortcuts import render, redirect
from .forms import SignUpForm, UserInfoForm, UserProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}! You can log in now')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserInfoForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'u_form':user_form, 'p_form':profile_form})


class LogIn(LoginView):
    template_name = 'users/login.html'


class LogOut(LogoutView):
    template_name = 'users/logout.html'