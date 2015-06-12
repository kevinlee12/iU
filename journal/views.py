from django.shortcuts import render


def index(request):
    return render(request, 'journal/home.html')


def welcome(request):
    name = "Person"
    return render(request, 'journal/welcome.html', {'name': name})
