from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from datetime import datetime
from django.utils import timezone

from main.models import Post

class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Post.objects.all()
        context['time'] = datetime.now()
        return context
    
class PostPreLoadTaskView(RedirectView):
    pattern_name = 'main:SinglePostView'
    def get_redirect_url(self,*args,**kwargs):
        # post = get_object_or_404(Post,pk=kwargs['pk'])
        post = Post.objects.filter(pk=kwargs['pk'])
        post.update_counter()
        return super().get_redirect_url(*args,**kwargs)
    
class SinglePostView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post,pk=self.kwargs.get('pk'))  
        return context
    
    
# class ArticleCounterRedirectView(RedirectView):
#     permanent = False
#     query_string = True
#     pattern_name = "article-detail"
    
#     def get_redirect_url(self,*args,**kwargs):
#         article = get_object_or_404(Post,pk = kwargs['pk'])
#         article.update_counter()
#         return super().get_redirect_url(*args,**kwargs)
