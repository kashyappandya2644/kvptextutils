from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    countchar=request.POST.get('countchar','off')
    if(removepunc=='on'):
        punct='''!@#$%^&*(){}[]""''?'''
        analyzed=''
        for i in djtext:
            if i not in punct:
                analyzed=analyzed+i
        para={'purpose':'Remove Punc','analyzetext':analyzed}
        djtext=analyzed

    if(uppercase=='on'):
        analyzed=''
        for i in djtext:
            analyzed=analyzed+i.upper()
        para={'purpose':'UpperCase','analyzetext':analyzed}

        djtext=analyzed
    if(countchar=='on'):
        analyzed=len(djtext)
        
        para={'purpose':'Countchar','analyzetext':analyzed}
    if(countchar!='on' and uppercase!='on' and removepunc!='on'):
        return HttpResponse('error')
    return render(request,'analyze.html',para)
