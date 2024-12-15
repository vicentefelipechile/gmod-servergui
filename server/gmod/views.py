from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def PageIndex(request: WSGIRequest) -> HttpResponse:
    return render(request, "index.html")

def PageLogin(request: WSGIRequest) -> HttpResponse:
    return render(request, "login.html")

@login_required(login_url="/login/steam/")
def PagePlayers(request: WSGIRequest) -> HttpResponse:
    return render(request, "players.html")