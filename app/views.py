from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def django_form(request):
    ENFO = NameForm()
    d = {'ENFO':ENFO}

    return render(request,'django_form.html',d)