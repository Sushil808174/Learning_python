from django.shortcuts import render,redirect
from .models import Users

def showrecord(request):
    data = Users.objects.all()
    print(data)
    return render(request,'showrecord.html',{'data':data})

def register(request):
    first_name = "Susheel"
    last_name = "Kumar"
    email = "sushil@gmail.com"
    phone = '7390849388'
    address = "Banki"
    city = "Hamirpur"
    state = "Uttar Pradesh"
    pincode = "210503"
    
    data = Users(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,city=city,state=state,pincode=pincode)
    data.save()
    return redirect('showrecord')
def update(request,id):
    data = Users.objects.get(id=id)
    data.address = 'Kalauli'
    data.save()
    return redirect('showrecord')

def delete(request , id):
    data = Users.objects.get(id=id)
    data.delete()
    return redirect('showrecord')