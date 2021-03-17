from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'gene/home.html')

def password(request):
    
    characters = list('sdfgnbjkfgijgkdfm,')

    if request.GET.get('uppercase'):
        characters.extend(list('ASFNKJEFHIUTBVNCBVHDGFUIQP'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()~'))


    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request,'gene/password.html', {'password' : thepassword} )

def about(request):
    return render(request,'gene/about.html')