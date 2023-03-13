# I have created it
from django.http import  HttpResponse
from django.shortcuts import render

def analyze(request):
    removepunc = request.POST.get('removepunc', 'off')
    Capitalized = request.POST.get('Capitalized', 'off')
    newline = request.POST.get('newline', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    text = request.POST.get('text','default')
    if text == "":
        return render(request,"error.html")

    elif (spaceremove != 'on' and Capitalized != 'on' and newline != 'on' and removepunc != 'on'):
        return render(request, "error1.html")
    else:

        print(removepunc)
        if removepunc == "on":
    
            analyzed = ""
            puntuations = '''!()-[]{};:'"\,<>./?^#$%&*_~'''

            for char in text:
                if char not in puntuations:
                    analyzed = analyzed + char
            # param = {'purpose':'Removed Puntuations','analyzed_text':analyzed}
            text = analyzed
        if newline == "on":
            analyzed = ""

            for char in text:
                if char != "\n" and char != '\r':
                    analyzed = analyzed + char
            # param = {'purpose':'Removed New Line Character','analyzed_text':analyzed}
            text = analyzed


        if Capitalized == "on":
            analyzed = ""

            for char in text:
                analyzed = analyzed + char.upper()
            # param = {'purpose':'Capitalized','analyzed_text':analyzed}
            text = analyzed
        if spaceremove == "on":
            analyzed = ""
            for index,char in enumerate(text):
                if not(text[index]==' ' and text[index+1]==' '):
                    analyzed = analyzed + char
            # param = {'purpose':'Extra Spaces removed','analyzed_text':analyzed}
        param = {'purpose': 'Extra Spaces removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

def index(request):
    return render(request,'index.html')

