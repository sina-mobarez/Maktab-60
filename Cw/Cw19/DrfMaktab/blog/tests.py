from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from rest_framework.test import APITestCase

from blog.models import Post, User


class TestPost(APITestCase):
    def setUp(self):
        # user = User(username='usr', password='usr')
        # user.save()
        # post1 = Post(title = 'post title1', creator=user)
        # post1.save()
        # post2 = Post(title = 'post title2', creator=user)
        # post2.save()
        # post3 = Post(title = 'post title3', creator=user, published=True)
        # post3.save()
        user = mommy.make(User)
        mommy.make(Post, published=True, creator=user,_quantity=10)
        mommy.make(Post, published=True, _quantity=10)
        
        
    def test_post_list(self):
        url = reverse('post_list')
        response = self.client.get(url)
        post_response = self.client.post(url, data={"title":"amin"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(post_response.data["title"], "amin")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 20)
