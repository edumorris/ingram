from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image
from django.contrib.auth.decorators import login_required

from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    latest_pics = Image.objects.all().order_by('-id')

    current_user = request.user

    return render(request, 'home.html', {"latest_pics": latest_pics, "current_user": current_user})

@login_required(login_url='/accounts/login')
def profile(request, user_id):
    imgs = Image.objects.filter(profile = user_id)
    current_user = request.user

    return render(request, 'profile.html', {"current_user": current_user, "imgs": imgs})

def index_test(request):
    title = "ingram index page testpage"

    return render(request, 'index.html', {"title": title})

# Complete email