from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<slug:current_article>/', ArticleDetailView.as_view(), name='one_article'),
    path('article/<slug:slug>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('tags/', TagsListVies.as_view(),  name='tags'),
    path('tags/<int:id>', ArticleDetailView.as_view(),  name='tag'),


]
