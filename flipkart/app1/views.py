from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hi!!! Nakshatra Degish")

def test_fun(request):
    return render(request,'test.html')

def demo_fun(request):
    return render(request,'demo2.html')
