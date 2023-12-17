from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'intro.html')

def aboutMe(request):
    return HttpResponse("this is about")