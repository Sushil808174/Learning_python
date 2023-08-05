from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def good_bye(request):
    return HttpResponse("Goodbye, World!")