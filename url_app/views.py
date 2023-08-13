from django.shortcuts import render, redirect
from .models import short_urls

# Create your views here.

def Home(request, token):
    urls = short_urls.objects.all()
    print(urls.values())
    for i in urls:
        print(i)
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
