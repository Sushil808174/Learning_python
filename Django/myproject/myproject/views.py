from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    dict = {
        'list':['Himanshu','Susheel','Aman','Ankit']
    }
    return render(request,"index.html",dict)
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def good_bye(request):
    return HttpResponse("Goodbye, World!")