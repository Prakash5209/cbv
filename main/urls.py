from django.urls import path
from django.views.generic import RedirectView
from main.views import HomeTemplateView,PostPreLoadTaskView,SinglePostView,PostDetailView
app_name = "main"

urlpatterns = [
    path('',HomeTemplateView.as_view(),name="HomeTemplateView"),
    path('ex3/<int:pk>/',PostPreLoadTaskView.as_view(),name="PostPreLoadTaskView"),
    path('about/<int:pk>.',SinglePostView.as_view(),name="SinglePostView"),
]