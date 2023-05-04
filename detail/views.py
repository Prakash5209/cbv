from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.utils import timezone

from detail.models import Books

class IndexView(TemplateView):
    template_name = "book.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Books.objects.all()
        context['date'] = timezone.now()
        return context
    
    
class BookDetailView(DetailView):
    model = Books
    # default variable to hold data = object
    context_object_name = 'bookdetail'
  
    