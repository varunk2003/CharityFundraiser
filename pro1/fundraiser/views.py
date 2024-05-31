from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template =loader.get_template('index.html')
    return   HttpResponse(template.render())    

def login(request):
    template =loader.get_template('login.html')
    return   HttpResponse(template.render({},request))

def signup(request):
    template =loader.get_template('signup.html')
    return   HttpResponse(template.render())

def back(request):
    return redirect('login')

@csrf_exempt
def createuser(request):
    users = request.POST['username']
    password1 = request.POST['password1']
    email = request.POST['email']
    password2= request.POST['password2']

    if password1 == password2:
        load = user(username = users,password1 = password1,email = email)
        load.save()
        return redirect('login')
    else:
        return HttpResponse("password are not match")

def signin(request):
    email=request.POST['emailid']
    password=request.POST['pass']
    data=user.objects.filter(email=email)
    if data:
        data=user.objects.get(email=email)
        if data.password1==password:
            load=log.objects.get(id=1)
            load.signins=True
            load.username=data.username
            load.emailid=email
            load.save()
            return redirect(index)
        else:
            return HttpResponse("Incorrect password")
    else:
        return HttpResponse("Username not found")

def logout(request):
    load=log.objects.get(id=1)
    load.signins=False
    load.save()
    return redirect('index.html')

