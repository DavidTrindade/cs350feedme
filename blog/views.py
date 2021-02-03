from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Feed


def home(request):

    context = {
        'feeds': Feed.objects.all(),
        'title': "Home"
    }

    if request.user.is_authenticated:
        context['favs'] = Feed.objects.filter(favourite=request.user)
    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

def faves(request):

    context = {
        'feeds': Feed.objects.filter(favourite=request.user),
        'title': "Favourites"
    }

    return render(request, 'blog/favourites.html', context)

def fav(request, id):
    feed = get_object_or_404(Feed, id=request.POST.get('feed_id'))
    if feed.favourite.filter(id=request.user.id).exists():
        feed.favourite.remove(request.user)
    else:
        feed.favourite.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
