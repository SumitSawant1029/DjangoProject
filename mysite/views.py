# I have created it
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'harry','place':'USA'}
    return render(request,'index.html',params)
    # return HttpResponse("Hello")

def about(request):
    return   HttpResponse('''<h1>Hello World</h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Helllooo</a>"''')