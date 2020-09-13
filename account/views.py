from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 


# Create your views here.
def registerview(request):
    message = ""
    if request.method == "POST":
        uname = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            user = User.objects.create_user(
                username=uname,
                email=email,
                password=pass1,
                first_name=fname,
                last_name=lname
            )
            user.save()
            print('user created.')
            return HttpResponseRedirect(reverse('loginview'))
        else:
            message = "Invalid password. Your error could be your password is not same as the confirm password, password should be more than 8 characters, and must not the same as username."
            return render(request, 'account/register.html', { 'message': message }) 
    return render(request, 'account/register.html')

def loginview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('todolist'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('todolist'))
        else:
            return render(request, 'account/login.html', {
                'message': "Invalid username or password.",
            })
    return render(request, 'account/login.html')
    
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginview'))
