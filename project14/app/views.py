from django.shortcuts import render
from .forms import *
from django.http import HttpResponse

# Create your views here.


def register(request):
    EPFO = ProfileForm()
    d = {'EPFO': EPFO}
    if request.method == 'POST' and request.FILES:
        PFDO = ProfileForm(request.POST, request.FILES)
        if PFDO.is_valid():
            PFDO.save()
            return HttpResponse('Done....')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)