from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    latest_pics = Image.objects.all().order_by('-id')

    return render(request, 'home.html', {"latest_pics": latest_pics})

@login_required(login_url='/accounts/login')
def profile(request):
    return render()

def index_test(request):
    title = "ingram index page testpage"

    return render(request, 'index.html', {"title": title})
