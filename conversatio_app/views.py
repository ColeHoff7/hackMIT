from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, '/conversatio_app/index.html')
# Create your views here.
