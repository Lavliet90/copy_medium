from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('<slug:slug>/', ArticleDetailView.as_view(),  name='article'),


]
