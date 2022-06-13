from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.core.mail import  send_mail
from django.conf import settings
from django.core.paginator import  Paginator
from .models import  *
from .forms import *


class ArticleListView(View):
    template_name = 'blog_app/article.html'
    articles = Article.objects.all()

    def get(self, request, *args, **kwargs):
        page = 1
        if request.GET.get('page')!=None:
         page=request.GET.get('page')
         page=int(page)

        dd = Paginator(self.articles,5)
        articles = dd.get_page(page)
        return render(request, self.template_name, {'articles': articles}) #{'articles':self.queryset})


class ArticleDetailView(View):
    template_name = 'blog_app/article_detail.html'

    def get(self, request, id, *args , **kwargs):
        article = Article.objects.get(id=id)
        return render(request, self.template_name, {'article': article})


class ContactView(View):
    template_name = 'blog_app/request_contact.html'
    email_subject = 'a message'
    email_message = 'the message'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['obide1@yahoo.com']

      
    def get(self, request, *args, **kwargs):
        form = ContactRequestForm()
        print(form)
        return render(request, self.template_name, {'form':form})

    def post(self,request, *args, **kwargs):
        data = request.POST
        form = ContactRequestForm(data)
        print(dir(form))
        if form.is_valid():
            print('here')
            form.save()
            send_mail(self.email_subject, self.email_message, self.email_from, self.recipient_list )
            
            return redirect('article_list_view')
        else:
            return HttpResponse(str(form.errors))   