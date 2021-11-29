from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

from blog.models import Post
from model_mommy import mommy

User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        # user = User(username='dev', password='123')
        # user.save()
        # post1 = Post(title='post title1', creator=user, published=True)
        # post1.save()
        # post2 = Post(title='post title2', creator=user)
        # post2.save()
        # post3 = Post(title='post title3', creator=user, published=True)
        # post3.save()

        user = mommy.make(User)
        mommy.make(Post, published=True, creator=user, _quantity=10)
        mommy.make(Post, published=False, _quantity=5)

    def test_post_list(self):
        url = reverse('post_list')

        resp = self.client.get(url)
        post_response = self.client.post(url, data={"title":"test2"})

        #print(resp.json())
        print(post_response.json())


        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data["title"], "test2")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 10)

