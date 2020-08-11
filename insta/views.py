from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

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

@login_required(login_url='/accounts/login')
def profile_update(request, user_id):

    title = 'Update Profile'
    current_user = request.user

    email = current_user.email

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            about = form.cleaned_data['bio']
            mobile = form.cleaned_data['phone_number']
            dp = form.cleaned_data['profile_photo']

            profile = Profile(user = current_user.id, first_name = fname, last_name = lname, email = current_user.email, bio = about, phone_number = mobile, prof_photo = dp)

            profile.save()
    else:
        form = ProfileForm()
    
    return render(request, 'profile_update.html', {"ProfileForm": form, "title": title})

def index_test(request):
    title = "ingram index page testpage"

    return render(request, 'index.html', {"title": title})