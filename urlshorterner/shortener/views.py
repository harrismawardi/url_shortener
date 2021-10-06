from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Shortener
from .forms import ShortenerForm

# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ShortenerForm(req.POST)
        if form.is_valid():
            shortened_object = form.save()
            new_url = req.build_absolute_uri('/') + 'api/' + shortened_object.short_url
            messages.success(req, new_url)
            return render(req, 'home.html')
    else:
        form = ShortenerForm()
    data = {'form': form}
    return render(req, 'home.html', data)

def url_redirect(req, short_url):
    try:
        shortener = Shortener.objects.get(short_url=short_url) 
        return redirect(shortener.long_url)
    except:
        return redirect(req.build_absolute_uri('/') + 'api/')