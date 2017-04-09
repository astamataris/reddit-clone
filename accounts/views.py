from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'message':'Username already exists'} )
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                login(request,user)
                return render(request,'accounts/signup.html' ,{'message':'user created'})
        else:
            return render(request,'accounts/signup.html',{'message':'passwords didn\'t match'} )
    else:
        return render(request,'accounts/signup.html' )

def login_reddit(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')

        else:
            return render(request, 'accounts/login.html',{'message': 'Username & password did not match'})
    else:
        return render(request,'accounts/login.html' )

def logout_reddit(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')