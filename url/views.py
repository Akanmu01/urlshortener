from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Link
from .forms import LinkForm
from django.views.generic import ListView

# Create your views here.
def home(request):
    BASE_URL = request.get_raw_uri()
    # return HttpResponse('Site is working')
    form = LinkForm(request.POST or None)
    if form.is_valid():
        form.save()
        key = form.cleaned_data.get('key')
        messages.success(request, f"URL has been successfully shortened to {BASE_URL}{key}")
        return redirect('home')
    return render(request, 'home.html', {"form": form})

def how_to(request):
    return render(request, 'how.html')


def redirector(request, key):
    instance = get_object_or_404(Link, key= key)
    return redirect(instance.original_url)