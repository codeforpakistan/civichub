from django.shortcuts import render
from django.http import HttpResponse
from app import models


def index(request):
    items = models.Activity.objects.all()
    hubs  = models.Hub.objects.all()

    return render(request, "app/index.html", context = {
        "activities": items,
        'hubs': hubs,
    })

def explore(request):
    items = models.Activity.objects.all()
    hubs  = models.Hub.objects.all()

    return render(request, "app/explore.html", context = {
        "activities": items,
        'hubs': hubs,
    })

def nearby(request):
    items = models.Activity.objects.all()
    hubs  = models.Hub.objects.all()

    return render(request, "app/nearby.html", context = {
        "activities": items,
        'hubs': hubs,
    })

def hub_list(request):
    items = models.Hub.objects.all()
    return render(request, "app/hub_list.html", context = {"hubs": items})

def hub_detail(request, hub):
    items = models.Activity.objects.filter(hubs__slug=hub).all()
    hubs  = models.Hub.objects.all()
    hub   = models.Hub.objects.get(slug=hub)

    return render(request, "app/hub_detail.html", context = {
        "activities": items,
        'hubs': hubs,
        'hub' : hub,
    })

def activity_detail(request, activity):
    item = models.Activity.objects.get(slug=activity)
    hubs  = models.Hub.objects.all()

    return render(request, "app/activity_detail.html", context = {
        "activity": item,
        'hubs': hubs,
    })

def user_detail(request, username):
    item = models.Profile.objects.get(user__username=username)
    hubs  = models.Hub.objects.all()

    return render(request, "app/user_detail.html", context = {
        "user": item,
        'hubs': hubs,
    })