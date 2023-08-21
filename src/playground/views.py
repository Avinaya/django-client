from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return render(request,'home.html', {'name':'Avinaya Acharya'})

 
def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1+ val2
    return render(request,'result.html',{'result':res})

def admin(request):
    return render(request,'admin.html')

