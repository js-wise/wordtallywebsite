from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def finishedCount(request):
    alltext = request.GET['alltext']
    allwords = alltext.split()
    total = len(allwords)
    wordcount = {}
    for word in allwords:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    uniquewords = len(wordcount)
    topwordcount = 0
    topword = ''
    for word in wordcount:
        if wordcount[word] > topwordcount:
            topwordcount = wordcount[word]
            topword = word

    return render(request, 'finishedCount.html', {'total': total, 'text': alltext, 'words': uniquewords, 'topword': topword, 'times': topwordcount})