from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def PageIndex(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def PagePlayers(request):
    return render(request, "players.html")