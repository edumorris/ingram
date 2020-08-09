from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    return render()

@login_required(login_url='/accounts/login')
def profile(request):
    return render()
