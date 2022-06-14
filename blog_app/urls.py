from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list_view'),
    path('article_list_view/', views.ArticleListView.as_view(), name='article_list_view'),
    path('article_detail_view/<slug:slug>/<int:id>/', views.ArticleDetailView.as_view(), name='article_detail_view'),
    path('contact_view/', views.ContactView.as_view(), name='contact_view'),
]