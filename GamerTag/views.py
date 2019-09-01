from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if request.COOKIES.has_key('login'):
        return render(request, "GamerTag/template/home.html")
    return render(request, "GamerTag/template/login.html")