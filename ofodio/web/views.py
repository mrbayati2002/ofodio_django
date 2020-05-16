from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.conf import settings

def home(request):
    context = {'movies': Movie.objects.all()}
    return render(request, 'home.html', context)

def player(request):
	context = {'media': settings.MEDIA_URL}
	return render(request, 'player.html', context)