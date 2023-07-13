from django.http import HttpResponse
import string
from django.shortcuts import render#from html css files templates 

def index(request):
    
    return render(request,'index.html')
 
def analyze(request):
    djtext = request.POST.get('text','default')
    
    removepunc = request.POST.get('removepunc','off')
    fullcapss = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    punc = string.punctuation
    analyzed = ''
    purpose = ''
    
    if removepunc == 'on':
        analyzed = ''
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}   
        djtext = analyzed
        purpose += " and Removed Punctuation"
        
    
    
    if fullcapss == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UpperCase'+purpose,'analyzed_text': analyzed}  
        djtext = analyzed
        purpose += " and Changed to UpperCase"
       
    
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                print('pre',analyzed)
        params = {'purpose':'New Line Removed'+purpose,'analyzed_text': analyzed}
        djtext = analyzed
        purpose += " and New Line Removed"
        
            
    if extraspaceremover == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
                
            
        params = {'purpose':'Extra Space Removed'+purpose,'analyzed_text': analyzed}
        djtext = analyzed
        purpose +=" and Extra Space Removed"
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcapss!="on"):
        analyzed = ''
        params = {'purpose':'Analyzed fail','analyzed_text': analyzed}
        return render(request,'analyze.html',params)
       
    return render(request,'analyze.html',params)   
    
    
    
