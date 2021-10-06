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
            new_url = req.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            messages.success(req, new_url)
            return render(req, 'home.html')
    else:
        form = ShortenerForm()
    data = {'form': form}
    return render(req, 'home.html', data)

def redirect(req, short_url):
    shortener = get_object_or_404(Shortener, short_url=short_url)
    return redirect(shortener.long_url)