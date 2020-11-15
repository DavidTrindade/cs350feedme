from django.shortcuts import render
from django.http import HttpResponse

feeds = [
    {
        'link': "http://www.theclumsytraveler.com/feed",
        'title': "The Clumsy Traveler",
        'desc': "Female Travel & Lifestyle Blog"
    },
    {
        'link': "http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml",
        'title': "BBC News - World",
        'desc': "BBC News - World"
    }
]

def home(request):

    context = {
        'feeds': feeds,
        'title': "Home"
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})