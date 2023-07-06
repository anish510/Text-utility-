from django.http import HttpResponse
import string
from django.shortcuts import redirect,render#from html css files templates 

def index(request):
    
    return render(request,'index.html')
 
def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(djtext)
    print(removepunc)
    punc = string.punctuation
    analyzed = ''
    if removepunc == 'on':
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}   
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

def capfirst(request):
    return HttpResponse("capitalize first")