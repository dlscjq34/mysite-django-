from django.shortcuts import render
from django.http import HttpResponse

#poll/urls.py에서 호출함
def index(request):
    return HttpResponse('hello, python')
