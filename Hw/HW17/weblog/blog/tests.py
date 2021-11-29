from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from blog.serilizers import *


# Create your tests here.

class TestPost(APITestCase):

    def setUp(self):
        user = mommy.make(User)
        user1 = User(1)
        mommy.make(Post, posted_by=user1)
        mommy.make(Post, posted_by=user, _quantity=4)

    def test_post_list(self):
        url = reverse('api_post_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    def test_post_details(self):
        user = User(username='usr', password='usr')
        user.save()
        mommy.make(Post, posted_by=user)
        response = self.client.get(reverse("api_post_details", kwargs={"post_id": 6}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["posted_by"]["username"], "usr")

    def test_comment_list(self):
        mommy.make(Comment, _quantity=3)
        response = self.client.get(reverse('api_comment_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_comment_details(self):
        mommy.make(Comment, body='salam')
        mommy.make(Comment, _quantity=4)
        response = self.client.get(reverse('api_comment_details', kwargs={"id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        response2 = self.client.get(reverse('api_comment_details', kwargs={"id": 7}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_category_list(self):
        mommy.make(Category, _quantity=12)
        response = self.client.get(reverse('api_category_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 12)

    def test_category_details(self):
        mommy.make(Category, name='yummy')
        mommy.make(Category, _quantity=3)
        response = self.client.get(reverse('api_category_details', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        response2 = self.client.get(reverse('api_category_details', kwargs={"pk": 7}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['name'], 'yummy')

    def test_tag_list(self):
        mommy.make(Tag, _quantity=55)
        response = self.client.get(reverse('api_tag_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 55)

    def test_tag_details(self):
        mommy.make(Tag, name='corona')
        mommy.make(Tag, _quantity=2)
        response = self.client.get(reverse('api_tag_details', kwargs={'tag_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        response2 = self.client.get(reverse('api_tag_details', kwargs={"tag_id": 7}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['name'], 'corona')
