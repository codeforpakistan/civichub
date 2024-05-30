from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("explore/", views.explore, name="explore"),
    path("nearby/", views.nearby, name="nearby"),
    path("h/", views.hub_list, name="hub_list"),
    path("h/<slug:hub>/", views.hub_detail, name="hub_detail"),
    path("a/<slug:activity>/", views.activity_detail, name="activity_detail"),
    path("a/<slug:activity>/like/", views.activity_like, name="activity_like"),
    path("a/<slug:activity>/unlike/", views.activity_unlike, name="activity_unlike"),
    path("a/<slug:activity>/comment/", views.activity_comment, name="activity_comment"),
    path("u/<slug:username>/", views.user_detail, name="user_detail"),
    path("c/<int:comment>/", views.comment_delete, name="comment_delete"),
]