from django.shortcuts import render
from django.http import HttpResponse

#poll/urls.py���� ȣ����
def index(request):
    return HttpResponse('hello, python')
