from django.shortcuts import render
from django.views.generic import ListView,DetailView

from Listview.models import ListModel,Status

class ListHome(ListView):
    model = ListModel
    
    
class ListDetail(DetailView):
    model = ListModel

    