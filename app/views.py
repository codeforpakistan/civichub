from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from app import models
from app import forms


def index(request):
    page_number = request.GET.get("page", 1)

    items = models.Activity.objects.order_by('-created_at').all()
    paginator = Paginator(items, per_page=12)
    page_object = paginator.get_page(page_number)
    hubs  = models.Hub.objects.all()

    return render(request, "app/index.html", context = {
        "activities": page_object,
        'hubs': hubs,
    })


def nearby(request):
    items = models.Activity.objects.all()
    hubs  = models.Hub.objects.all()

    return render(request, "app/nearby.html", context = {
        "activities": items,
        'hubs': hubs,
    })

        # items = models.Hub.objects.all()
        # return render(request, "app/hub_list.html", context = {"hubs": items})


class HubList(ListView):
    def get(self, request):
        items = models.Activity.objects.all()
        hubs  = models.Hub.objects.all()

        return render(request, "app/explore.html", context = {
            "activities": items,
            'hubs': hubs,
        })


class HubDetail(View):
    model = models.Hub
    template_name = "app/hub/detail.html"

    def get(self, request, hub):
        items = models.Activity.objects.filter(hubs__slug=hub).all()
        hubs  = models.Hub.objects.all()

        return render(request, "app/hub/detail.html", context = {
            "activities": items,
            'hubs': hubs,
        })


def activity_items(request):
    page_number = request.GET.get("page", 1)
    items = models.Activity.objects.order_by('-created_at').all()
    paginator = Paginator(items, per_page=12)
    page_object = paginator.get_page(page_number)

    return render(request, "app/activity/grid.html", {
        'activities': page_object
    })


class ActivityList(View):
    def get(self, request):
        page_number = request.GET.get("page", 1)
        items = models.Activity.objects.order_by('-created_at').all()
        paginator = Paginator(items, per_page=12)
        page_object = paginator.get_page(page_number)

        hubs  = models.Hub.objects.all()

        return render(request, "app/activity/list.html", context = {
            "activities": page_object,
            'hubs': hubs,
        })
    
    def submit(request):
        hubs  = models.Hub.objects.all()
        return render(request, "app/activity/form.html", context = {
            'hubs': hubs,
        })
        
    def post(self, request): 
        
        if request.method == 'POST':
            form = forms.ActivityForm(request.POST)
            if form.is_valid():
                activity = form.save(commit=False)
                activity.slug = slugify(activity.name)
                activity.user = request.user
                activity.save()

                response = HttpResponse()
                response["HX-Redirect"] = reverse('app:activity_detail', kwargs={'activity': activity.slug})
                return response
            else:
                print(form.is_valid())
                print(form.errors)
            return redirect(reverse('app:activity_list'), { 'form': form })
        return None


class ActivityDetail(View):
    def get(self, request, activity):
        item = models.Activity.objects.get(slug=activity)
        hubs  = models.Hub.objects.all()

        return render(request, "app/activity/detail.html", context = {
            "activity": item,
            'hubs': hubs,
        })
    
    def put(self, request, activity):
        pass

    def delete(self, request, activity):
        activity = models.Activity.objects.get(slug=activity)
        activity.delete()

        response = HttpResponse()
        response["HX-Redirect"] = reverse('app:home')
        return response


class activity_create(View):
    def get(self, request):
        hubs  = models.Hub.objects.all()
        return render(request, "app/activity/form.html", context = {
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

    return render(request, "app/activity/partials/unlike.html", {
        'activity': activity
    })

def activity_unlike(request, activity):
    activity = models.Activity.objects.get(slug=activity)
    activity.likes -= 1
    activity.save()

    return render(request, "app/activity/partials/like.html", {
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

class CommentList(View):
    def post(self, request):
        pass

class CommentDetail(View):
    def get(self, request, comment):
        pass
    
    def delete(self, request, comment):
        comment = models.Comment.objects.get(pk=comment)
        activity = comment.activity
        comment.delete()

        return render(request, 'app/comment/list.html', {
            'comments': activity.comments.all()
        })