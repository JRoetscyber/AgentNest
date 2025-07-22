from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def home_page(request):

    return render(request, "home_page.html")