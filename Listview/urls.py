from django.urls import path

from Listview.views import ListHome,ListDetail

app_name = "Listview"
urlpatterns = [
    path('',ListHome.as_view(),name="ListHome"),
    path('list_description/<int:pk>/',ListDetail.as_view(),name="ListDetail"),
]