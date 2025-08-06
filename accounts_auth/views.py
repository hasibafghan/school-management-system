from django.shortcuts import render , redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm , LoginForm



def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup is successful')
            return redirect('student_list')
        else:
            messages.error(request, 'Signup failed — please fix the errors below.')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts_auth/signup.html', {'form': form})




def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request , 'accounts_auth/login.html' , {'form' : form})


def logout_view(request):
    logout(request)
    messages.success(request , 'Logout successfully')
    return redirect('login')