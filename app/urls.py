from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path("", views.index, name="home"),
    path("explore/", views.HubList.as_view(), name="explore"),
    path("nearby/", views.nearby, name="nearby"),
    path("submit/", views.ActivityList.submit, name="submit"),
    path("h/", views.HubList.as_view(), name="hub_list"),
    path("h/<slug:hub>/", views.HubDetail.as_view(), name="hub_detail"),
    path("a/", views.ActivityList.as_view(), name="activity_list"),
    path("a/items", views.activity_items, name="activity_items"),
    path("a/<slug:activity>/", views.ActivityDetail.as_view(), name="activity_detail"),
    path("a/<slug:activity>/like/", views.activity_like, name="activity_like"),
    path("a/<slug:activity>/unlike/", views.activity_unlike, name="activity_unlike"),
    path("a/<slug:activity>/comment/", views.activity_comment, name="activity_comment"),
    path("u/<slug:username>/", views.user_detail, name="user_detail"),
    path("u/<slug:username>/achievements", views.user_detail, name="achievements"),
    path("c/<int:comment>/", views.CommentDetail.delete, name="comment_delete"),
]