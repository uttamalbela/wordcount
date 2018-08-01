from django.http import HttpResponse
from django.shortcuts import render
import operator

def hello(request):
    return HttpResponse("Hello World")

def eggs(request):
    return HttpResponse("Gunjan loves egg whites.")

def home1(request):
    return render(request, 'home1.html',{'hithere':'Hello! This is Uttam'})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltextbyuser = request.GET["fulltext"]
    wordlist=fulltextbyuser.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedlist=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)
    #This prints in the console
    #print(fulltextbyuser)
    return render(request, 'count.html',{'fulltextinhtml':fulltextbyuser, 'wordcount': len(wordlist), 'worddictionary':worddictionary, 'wordlist':worddictionary.items(),'sortedlist':sortedlist})