from django.http import HttpResponse
import string
from django.shortcuts import redirect,render#from html css files templates 

def index(request):
    
    return render(request,'index.html')
 
def analyze(request):
    djtext = request.GET.get('text','default')
    
    removepunc = request.GET.get('removepunc','off')
    fullcapss = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    
    punc = string.punctuation
    analyzed = ''
    
    if removepunc == 'on' and fullcapss == 'off':
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}   
        return render(request,'analyze.html',params)
    
    
    elif fullcapss == 'on' and removepunc == 'off':
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UpperCase','analyzed_text': analyzed}  
        return render(request,'analyze.html',params)
    
    
    elif removepunc == 'on' and fullcapss == 'on':
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char.upper()
        params = {'purpose':'Removed Punctuations and Changed to UpperCase','analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    
    elif newlineremover == 'on':
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose':'New Line Removed','analyzed_text': analyzed}
        return render(request,'analyze.html',params)
            
    elif extraspaceremover == 'on':
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
                
            
        params = {'purpose':'Extra Space Removed','analyzed_text': analyzed}
        return render(request,'analyze.html',params)
        
    else:
        return HttpResponse("Error")
    
    
        

def capfirst(request):
    return HttpResponse("capitalize first")