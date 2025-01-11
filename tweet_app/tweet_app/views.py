from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

