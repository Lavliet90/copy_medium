from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<slug:slug>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(),  name='article'),
    # path('tags/', post_list, name='post_list'),
    # path('tags/<slug:slug>', post_list, name='post_list_by_tag'),


]
