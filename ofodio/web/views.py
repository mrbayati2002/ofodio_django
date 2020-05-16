from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.conf import settings

def home(request):
	# MM = Movie.objects.all()
	# for M in MM:
		# M.file = M.file.split('/')[1]
		# print(M.file, type(M), type(M.file))
	context = {'movies': Movie.objects.all()}
	return render(request, 'home.html', context)

def player(request, moviename):
	context = {'media': settings.MEDIA_URL,
				'moviename':moviename}
	return render(request, 'player.html', context)