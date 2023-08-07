from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    # dict = {
    #     'list':['Himanshu','Susheel','Aman','Ankit']
    # }
    dict = {}
    try:
        if request.method == 'POST':
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            sum = num1+num2
            dict={
                'n1':num1,
                'n2':num2,
                'sum':sum
            }
    except:
        pass        
    return render(request,"index.html",dict)
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def good_bye(request):
    return HttpResponse("Goodbye, World!")