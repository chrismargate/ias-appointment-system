from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    # return HttpResponse("<p>Hello</p>")
    return render(response,'index.html')

def careers(response):
    pass

def specialities(response):
    pass

def sustainable_dev(response):
    pass

def contact_us(response):
    pass

def about_us(response):
    pass

def login(response):
    pass

def register(response):
    pass

# Views once logged in

def dashboard(response):
    pass