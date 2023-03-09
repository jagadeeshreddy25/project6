from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('dhoni is best finesher')
def  raina(request):
    return HttpResponse('mr.ipl')