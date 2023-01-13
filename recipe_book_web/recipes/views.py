import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
"""
# Create your views here.
def home(request):
    return HttpResponse("Hello, here my recipe book will be located")
"""
def home(request):
    return render(request, "recipes/home.html")

def about(request):
    return render(request, "recipes/about.html")

def contact(request):
    return render(request, "recipes/contact.html")

def hello(request, name):
    return render(
        request,
        'recipes/hello.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

"""
def hello(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    content = "Hello " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
"""