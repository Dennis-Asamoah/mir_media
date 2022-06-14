from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


class TESTAPI(TestCase):
    @classmethod
    def setUpTestData(self):
        user1 = User(username='obide', email='2@gmailk.com', password='123456')
        user1.save()
        article1 = Article(title='Redux', content='contains boilerpaltes', author=user1)
        article1.save()
        self.url = reverse('article_list_view')
        self.url1 = reverse('article_detail_view', args=['redux', 1])
        self.url2 = reverse('contact_view')

    def test_article_list_get(self):
        response = self.client.get(self.url)
        # print (response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_detail_list_get(self):
        response = self.client.get(self.url1)
        # print (response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_contact_get(self):
        response = self.client.get(self.url2)
        # print (response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_contact_post(self):
        data = {"email": "o@gmail.com", "content": "is  cool", "name": 'o'} 
        response = self.client.post(self.url2, data)
        self.assertEqual(response.status_code, 302)  # when contact is insertes successfully there will be a redirect 

   