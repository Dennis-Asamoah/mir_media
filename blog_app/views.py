from django.shortcuts import render
from django.views import View
from .models import  *
from django.http import HttpResponse


class ArticleListView(View):
    template_name = 'blog_app/article.html'
    queryset =  article = Article.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'k':self.queryset})


class ArticleDetailView(View):
    template_name = 'blogs/article_detail.html'

    def get(self, request, pk, *args , **kwargs):
        article = Article.objects.get(pk=pk)
        return render(request, self.template_name, {'article': article})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self,request, *args, **kwargs):
        pass 






