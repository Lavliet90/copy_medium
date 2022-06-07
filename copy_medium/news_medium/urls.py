from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<slug:slug>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(),  name='article'),
    path('tags/', TagsListVies.as_view(),  name='tags'),


]
