# I have created it
from django.http import  HttpResponse
from django.shortcuts import render
# def hello(request):
#     return  HttpResponse('Hello')
# def return1(request):
#     return render(request,'return.html')
def analyze(request):

    text = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    Capitalized = request.GET.get('Capitalized','off')
    print(removepunc)
    if removepunc == "on":
    
        analyzed = ""
        puntuations = '''!()-[]{};:'"\,<>./?^#$%&*_~'''

        for char in text:
            if char not in puntuations:
                analyzed = analyzed + char
        param = {'purpose':'Removed Puntuations','analyzed_text':analyzed}
    elif Capitalized == "on":
        analyzed = ""

        for char in text:
            analyzed = analyzed + char.upper()
        param = {'purpose':'Capitalized','analyzed_text':analyzed}

    else:
        param = {'purpose':'Removed Puntuations','analyzed_text':text}
    return render(request,'analyze.html',param)

def index(request):
    params = {'name': 'harry','place':'USA'}
    return render(request,'index.html',params)


# def about(request):
#     return   HttpResponse('''<h1>Hello World</h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Helllooo</a>"''')

