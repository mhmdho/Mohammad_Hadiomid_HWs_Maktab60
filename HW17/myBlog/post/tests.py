from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

from post.models import Category, Comment, Post
from model_mommy import mommy

# Create your tests here.

User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        user = mommy.make(User, username='Mohammad')
        mommy.make(Post, status=True, author=user, _quantity=10)
        mommy.make(Post, title="first_post", author=user, _quantity=1)
        mommy.make(Post, status=False, _quantity=5)
        mommy.make(Comment, _quantity=6)
        mommy.make(Comment, owner=user, description="great post", _quantity=1)
        mommy.make(Category, _quantity=5)
        mommy.make(Category, title="cat_test", _quantity=1)

    def test_post_list(self):
        url = reverse('post_list_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 18)

    def test_post_detail(self):
        url = reverse('post_detail_api', args=[11])
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data['title'], "first_post")

    def test_post_detail_null(self):
        url = reverse('post_detail_api', args=[24])
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 404)


    def test_comment_list(self):
        url = reverse('comment_list_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 7)
    
    def test_comment_detail(self):
        url = reverse('comment_detail_api', args=[7])
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data['description'], "great post")
        self.assertEqual(post_response.data['owner']['username'], 'Mohammad')
    
    def test_comment_detail_null(self):
        url = reverse('comment_detail_api', args=[8])
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 404)


    def test_category_list(self):
        url = reverse('category_list_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 6)
    
    def test_category_detail(self):
        url = reverse('category_detail_api', args=[6])
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data['title'], "cat_test")
    
    def test_category_detail_null(self):
        url = reverse('category_detail_api', args=[7])
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 404)
