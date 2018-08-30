from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'home.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)

    return HttpResponse(c)


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(c)


# 让旧的（/add/4/4/）变新的(new_add/4/4)
def old_up(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
