# I have created this file - Shubham
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Shubham','place':'Muradnagar'}
    return render(request, 'index.html', params)

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')    
    # Analyze the text
    if removepunc == 'on':
        puncatuations = '''~`!@#$%^&*()_-+={[}]\|"':;?/>,.<'''
        analyze = ""
        for char in djtext:
            if char not in puncatuations:
                analyze = analyze + char 
        params = {'analyzed_text':analyze,'purpose':'Remove Puncs'}
        djtext = analyze

    if fullcaps == 'on':
        analyze = ''
        for char in djtext:
            analyze = analyze + char.upper()
        params = {'analyzed_text':analyze,'purpose':'Changed to Upper Case'}
        djtext = analyze

    if newlineremover == 'on':
        analyze = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyze = analyze + char
        params = {'analyzed_text':analyze,'purpose':'New Line Remover'}
        djtext = analyze

    if extraspaceremover == 'on':
        analyze = ''
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index + 1] == ' ':
                pass
            else:
                analyze = analyze + char
        params = {'purpose':'Removed Extra Spaces', 'analyzed_text':analyze}

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
        return HttpResponse('Please select any operation and try again')

    return render(request, 'analyze.html', params)
    
        