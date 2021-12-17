from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages
from .models import Netfeelex
from django.http import HttpResponse


# Create your views here.


def homepage(request):
    return render(request=request, template_name='main/home.html',
                  context={"netfeelex": Netfeelex.objects.all})
