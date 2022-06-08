from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'news_medium/main_page.html'
    context_object_name = 'articles'
    paginate_by = 5



    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return Article.objects.filter(status='publisher')