from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(request):
    return render(request,'intro.html')

def aboutMe(request):
    return HttpResponse("this is about")