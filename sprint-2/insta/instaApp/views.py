from django.shortcuts import render,HttpResponse
from .models import UserModel

def home(request):
    userModel = UserModel.objects.all()
    print(userModel)
    return render(request,"home.html",{'user':userModel})