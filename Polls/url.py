
from django.urls import path
from Polls import views

urlpatterns = [
    path('',views.Home),
    path("about/",views.aboutMe),
]
