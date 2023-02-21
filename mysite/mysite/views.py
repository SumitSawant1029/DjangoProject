# I have created it
from django.http import  HttpResponse


def index(request):
    return HttpResponse("Hello")

def about(request):
    return   HttpResponse("Hello Bro")