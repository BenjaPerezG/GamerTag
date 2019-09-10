from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset, 'games/index.html')