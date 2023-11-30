from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from django.contrib.admin.views.decorators import staff_member_required
# @staff_member_required

@login_required
def home_page(request):
    return render(request, "home/home.html")

