from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Feed
from .forms import FaveForm
from pathlib import Path
import numpy as np
import pandas as pd

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

    if request.method == 'POST':
        form = FaveForm(request.POST)
        if form.is_valid():
            feed = form.save()
            request.user.feeds.add(feed)
    else:
        form = FaveForm()

    context = {
        'feeds': Feed.objects.filter(favourite=request.user),
        'title': "Favourites",
        'form': form
    }

    return render(request, 'blog/favourites.html', context)

def fav(request, id):
    feed = get_object_or_404(Feed, id=request.POST.get('feed_id'))
    if feed.favourite.filter(id=request.user.id).exists():
        feed.favourite.remove(request.user)
    else:
        feed.favourite.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def feed(request, id):
    feed = get_object_or_404(Feed, id=id)
    # articles = feed.article_set.all()

    df = pd.read_csv(Path("../../dataframes")/"df_import.csv")

    with open(Path("../../")/"dist_mat.npy", 'rb') as f:
        dist_mat = np.load(f)

    indices = recommend(df, id, dist_mat)

    recommended = get_list_or_404(Feed, id__in=indices)
    recommended.sort(key=lambda feed: indices.index(feed.id))

    context = {
        'title': feed.title,
        # 'articles': articles,
        'feeds': recommended,
        'link': feed.link
    }

    return render(request, 'blog/feed.html', context)

def graph(request):
    return render(request, 'blog/graph.html', {'title': "Graph"})


def recommend(df, idx, dist_mat, title=""):
    if title != "":
        idx = df['title'][df['title'] == title].index[0]
    score_series = pd.Series(dist_mat[idx]).sort_values()
    top_10_indices = list(score_series.iloc[1:11].index)

    return top_10_indices

