from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article'),

]
