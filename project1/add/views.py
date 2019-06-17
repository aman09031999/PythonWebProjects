from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'login.html')

def login(request):

    user = request.POST["user"]
    password = request.POST["pass"]

    if user == "Aman" and password == "1234":
        return render(request,'home.html',{'name' : user})
    else:
        return render(request,"<h1><center>Wrong Credentials</center></h1>")

def home(request):
    return render(request,'home.html')

def add(request):

    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])

    result = val1 + val2

    return render(request,'result.html',{'result' : result})

def sub(request):

    val1 = int(request.GET["num3"])
    val2 = int(request.GET["num4"])

    result = val1 - val2

    return render(request,'result.html',{'result' : result})

def multiply(request):

    val1 = int(request.GET['num5'])
    val2 = int(request.GET['num6'])

    result = val1 * val2

    return render(request,'result.html',{'result' : result})

def divide(request):

    val1 = int(request.GET["num7"])
    val2 = int(request.GET["num8"])

    result = val1 / val2

    return render(request,'result.html',{'result' : result})

def logout(request):
    return render(request,'login.html')