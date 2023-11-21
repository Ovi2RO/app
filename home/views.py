from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_page(request):
    return render(request, "home/home.html")