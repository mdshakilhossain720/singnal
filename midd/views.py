from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    print('i am view ')
    return HttpResponse('This is the Home Page')
