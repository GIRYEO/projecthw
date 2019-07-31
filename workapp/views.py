from django.shortcuts import render, redirect
from accounts.models import Profile

# Create your views here.
def check(request):
    return render(request, 'check.html')

def checkcode(request):

        return render(request, 'checkcode.html')
