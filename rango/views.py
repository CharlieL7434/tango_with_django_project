from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #<a href='/rango/about/'>About,/a>
    context_dict = {'boldmessage' :'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #<a href='/rango/'>Index,/a>
    context_dict = {'boldmessage' :'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context=context_dict)
