from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def templates(request):
    return render(request,'templates_filters.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')