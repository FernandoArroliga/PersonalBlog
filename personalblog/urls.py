from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("post1/", views.post1, name="post1")
]