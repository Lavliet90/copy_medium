from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from taggit.models import Tag

from .models import Article, Comment, CategoryArticle


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




class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news_medium/article.html'
    context_object_name = 'article'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Article'
        context['comments'] = Comment.objects.filter(article=context.get('article'))[:5]
        print(context.get('article'))
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['name', 'email', 'comment_text', 'article']
    template_name = 'news_medium/add_comment.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add comment'
        return context


class TagsListVies(ListView):
    model = CategoryArticle
    template_name = 'news_medium/tags.html'
    context_object_name = 'tags'


# def post_list(request, tag_slug=None):
#     object_list = Article.objects.all()
#     tag = None
#     print('efefe')
#     print(request)
#     print(tag_slug)
#
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         object_list = object_list.filter(tags__in=[tag])
#
#         paginator = Paginator(object_list, 5)
#         page = request.GET.get('page')
#         try:
#             posts = paginator.page(page)
#         except PageNotAnInteger:
#             # If page is not an integer deliver the first page
#             posts = paginator.page(1)
#         except EmptyPage:
#             # If page is out of range deliver last page of results
#             posts = paginator.page(paginator.num_pages)
#         return render(request, 'news_medium/tags.html', {'page': page,
#                                                        'posts': posts,
#                                                        'tag': tag})
