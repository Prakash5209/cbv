from django.urls import path

from detail.views import IndexView,BookDetailView
app_name = "detail"
urlpatterns = [
    path('books/',IndexView.as_view(),name = "index"),
    path('books/<slug:slug>/',BookDetailView.as_view(),name="BookDetailView"),
    # path('<slug:slug>/',BookDetailView.as_view(),name="book_detail"),
]