from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,  UserUpdateForm, UserForm
from jobs.models import Job
from resumes.models import Resume, Application
from django.contrib.auth import get_user_model

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('home')
        
        return render(request, 'users/login.html', {'form':form})


class SignUpView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'users/sign-up.html', {'form':form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('my-profile')
        return render(request, 'users/sign-up.html', {'form':form})


class UserUpdateView(View):
    def get(self, request):
        if request.user.role == 'employer':
            base_template = 'emp-base.html'
        elif request.user.role == 'worker':
            base_template = 'worker-base.html'
        else:
            redirect('home')
        form = UserUpdateForm(instance=request.user)
        return render(request, 'users/update-profile.html', {'form': form, 'base_template':base_template})


    def post(self, request):
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('my-profile', request.user.username)
        return render(request, 'users/update-profile.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('home')



class UserDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/delete-account.html')

    def post(self, request):
        user = request.user
        user.delete()
        return redirect('home')
    
    
class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        if request.user.role == 'employer':
            base_template = 'emp-base.html'
            
            return render(request, 'users/profile.html', {'base_template': base_template})


        