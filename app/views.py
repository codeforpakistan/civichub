from django.shortcuts import render, redirect
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

    return render(request, "app/hub/detail.html", context = {
        "activities": items,
        'hubs': hubs,
        'hub' : hub,
    })

def activity_detail(request, activity):
    item = models.Activity.objects.get(slug=activity)
    hubs  = models.Hub.objects.all()

    return render(request, "app/activity/detail.html", context = {
        "activity": item,
        'hubs': hubs,
    })

def user_detail(request, username):
    user = models.User.objects.get(username=username)
    hubs  = models.Hub.objects.all()

    return render(request, "app/user/detail.html", context = {
        "user": user,
        'hubs': hubs,
    })

def activity_like(request, activity):
    activity = models.Activity.objects.get(slug=activity)
    activity.likes += 1
    activity.save()

    return render(request, "app/partials/unlike.html", {
        'activity': activity
    })

def activity_unlike(request, activity):
    activity = models.Activity.objects.get(slug=activity)
    activity.likes -= 1
    activity.save()

    return render(request, "app/partials/like.html", {
        'activity': activity
    })

def activity_comment(request, activity):
    activity = models.Activity.objects.get(slug=activity)
    models.Comment.objects.create(
        body=request.POST.get('body'),
        user=request.user,
        activity=activity
    )

    return render(request, 'app/comment/list.html', {
        'comments': activity.comments.all()
    })
    
    
def comment_delete(request, comment):
    comment = models.Comment.objects.get(pk=comment)
    activity = comment.activity
    comment.delete()

    return render(request, 'app/comment/list.html', {
        'comments': activity.comments.all()
    })