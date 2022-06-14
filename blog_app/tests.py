from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(self):
        user1 = User(username='dennis', email='obide1@yahoo.com', password='123456789')
        user1.save() 
        user2 = User(username='obide', email='obide1@gmail.com', password='123456')
        user2.save()
        article1 = Article(title='drf', content='drf is great', author=user1)
        article1.save()
        article2 = Article(title='Django2', content='django is great', author=user2)
        article2.save()
        contact_request = ContactRequest(email='k@gmail.com', name='k', content='good')
        contact_request.save()

    def test_article_read(self):
        article = Article.objects.get(id=1)
        author = User.objects.get(id=1)
        self.assertEqual(author.username, 'dennis')
        self.assertEqual(str(author.email),'obide1@yahoo.com')
        self.assertEqual(article.title, 'drf')
        self.assertEqual(article.content, 'drf is great')
        self.assertEqual(article.author, author) 
        self.assertEqual(str(author), 'dennis')

    def test_article_update(self):
        article = Article.objects.get(id=1)
        author = User.objects.get(id=1)
        article.title = 'django'
        #post.save()
        self.assertEqual(article.title, 'django')

    def test_article_delete(self):
        #k = reverse('posts')
        #print(k)
        article = Article.objects.get(id=1)
        user = Article.objects.get(id=2)
        article.delete()
        xx = Article.objects.filter(id=2)
        self.assertEqual(xx.count(), 1)
    
    def test_contact_read(self):
        contact_req = ContactRequest.objects.get(id=1)
        self.assertEqual(contact_req.email, 'k@gmail.com')
        self.assertEqual(contact_req.name, 'k')
        self.assertEqual(contact_req.content, 'good') 
    
    def test_contact_update(self):
        contact_req = ContactRequest.objects.get(id=1)
        contact_req.name = 'KO'
        #post.save()
        self.assertEqual(contact_req.name, 'KO')

    def test_article_delete(self):
        contact_req = ContactRequest.objects.get(id=1)
        contact_req.delete()
        xx = ContactRequest.objects.filter(id=1)
        self.assertEqual(xx.count(), 0)