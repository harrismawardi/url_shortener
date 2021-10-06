from django.shortcuts import render, redirect
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

def not_found_404(req, exception):
    return render(req, '404.html')

def server_error_500(req):
    return render(req, '500.html')