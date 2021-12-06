from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

from post.models import Category, Comment, Post, Tag
from model_mommy import mommy

# Create your tests here.

User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        self.user = mommy.make(User, username='Mohammad')
        mommy.make(Post, status=True, author=self.user, _quantity=10)
        mommy.make(Post, title="first_post", author=self.user, _quantity=1)
        mommy.make(Post, status=False, _quantity=5)
        mommy.make(Comment, _quantity=6)
        mommy.make(Comment, owner=self.user, description="great post", _quantity=1)
        mommy.make(Category, _quantity=5)
        mommy.make(Category, title="cat_test", _quantity=1)
        mommy.make(Tag, _quantity=2)

    def test_post_list(self):
        url = reverse('post_list_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 18)

    def test_post_detail(self):
        url = reverse('post_detail_api', args=[11])
        self.client.force_authenticate(self.user)

        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data['title'], "first_post")

    def test_post_detail_null(self):
        url = reverse('post_detail_api', args=[24])
        self.client.force_authenticate(self.user)
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 404)


    def test_comment_list(self):
        url = reverse('comment_list_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 7)
    
    def test_comment_detail(self):
        url = reverse('comment_detail_api', args=[7])
        self.client.force_authenticate(self.user)
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data['description'], "great post")
        self.assertEqual(post_response.data['owner']['username'], 'Mohammad')
    
    def test_comment_detail_null(self):
        url = reverse('comment_detail_api', args=[8])
        self.client.force_authenticate(self.user)
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 404)


    def test_category_list(self):
        url = reverse('category_list_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 6)
    
    def test_category_detail(self):
        url = reverse('category_detail_api', args=[6])
        self.client.force_authenticate(self.user)
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.data['title'], "cat_test")
    
    def test_category_detail_null(self):
        url = reverse('category_detail_api', args=[7])
        self.client.force_authenticate(self.user)
        post_response = self.client.get(url)
        self.assertEqual(post_response.status_code, 404)


    def test_create_post(self):
        url = reverse('createpost_api')

        tag = Tag.objects.first()
        category = Category.objects.first()
        data = {
                'title': 'test title',
                'tag': tag.id,
                'category' : category.id
                }
        
        self.client.force_authenticate(self.user)
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 201)
        post = Post.objects.get(id=resp.data['id'])
        self.assertEqual(post.author, self.user)
        self.assertTrue(post.status)
    

    def test_update_post(self):
        post = Post(author=self.user, title='test title 1')
        post.save()
        url = reverse('updatedeletepost_api', kwargs={'id': post.id})
        new_title = "update test"
        data =  {
                "title": new_title,
                "tag": Tag.objects.last().id,
                "category": Category.objects.last().id
                }

        self.client.force_authenticate(self.user)
        resp = self.client.put(url, data=data)


        self.assertEqual(resp.status_code, 200)

        updated_post = Post.objects.get(id=post.id)
        self.assertEqual(updated_post.title, new_title)


    def test_update_post_with_invalid_user(self):
        post = Post(author=self.user, title='test title')
        post.save()
        url = reverse('updatedeletepost_api', kwargs={'id': post.id})
        new_title = "new title"
        data = {
            "title": new_title,
            "tag": Tag.objects.last().id,
            "category": Category.objects.last().id
               }

        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)

        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 400)


    def test_delete_post(self):
        post = Post.objects.get(id=2)
        url = reverse('updatedeletepost_api', kwargs={'id':post.id})
        self.client.force_authenticate(self.user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(Post.objects.filter(id=post.id).exists())


    def test_delete_post_with_another_user(self):
        post = Post.objects.get(id=16)
        url = reverse('updatedeletepost_api', kwargs={'id':post.id})
        
        self.client.force_authenticate(self.user)
        # another_user = mommy.make(User)
        # self.client.force_authenticate(another_user)

        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(Post.objects.filter(id=post.id).exists())
