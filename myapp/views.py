from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is a basic Django app!")
