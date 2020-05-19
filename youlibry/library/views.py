from django.shortcuts import render
from django.http import HttpResponse
from .tasks import videos, channel_statistic


# Create your views here.

def index(request):
        stat_results = channel_statistic()

        context = {
                'stat_results' : stat_results
        }
        return render(request, 'index.html', context)


def resource(request):
    return render(request, 'libraries.html')


def resource(request):
    return render(request, 'libraries.html')

def trending(request):
    return render(request, 'trending.html')


def category(request):
    return render(request, 'categories.html')

def live(request):
    return render(request, 'live.html')

def explore(request):
    return render(request, 'explore.html')