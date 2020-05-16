from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    # path('player/', views.player),
    re_path(r'^player/(?P<moviename>\S{0,64})/$', views.player),
]