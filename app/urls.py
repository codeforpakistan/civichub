from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("explore", views.explore, name="explore"),
    path("nearby", views.explore, name="nearby"),
    path("h/", views.hub_list, name="hub_list"),
    path("h/<slug:hub>/", views.hub_detail, name="hub_detail"),
    path("a/<slug:activity>", views.activity_detail, name="activity_detail"),
    path("u/<slug:username>", views.user_detail, name="user_detail"),
]