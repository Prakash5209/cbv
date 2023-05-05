from django.shortcuts import render
from django.views.generic import ListView,DetailView

from Listview.models import ListModel,Status

class ListHome(ListView):
    model=ListModel
    def get_queryset(self,**kwargs):
        var=super().get_queryset(**kwargs).filter(status=Status.PUBLIC)
        return var
    
    
class ListDetail(DetailView):
    model=ListModel

    