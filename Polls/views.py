from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(request):
    return HttpResponse("hello , prithibi.You're amazing ")

def aboutMe(request):
    return HttpResponse("this is about")