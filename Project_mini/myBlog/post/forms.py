from django import forms
from django.forms import fields
from .models import  Tag,Category,Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if new_password != confirm_new_password:
            raise ValidationError('Two new passwords must be equal!')
        
        return confirm_new_password


class AddCategoryForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=3,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Add new category here'}))
    def save(self):
        Category.objects.create(title=self.cleaned_data['title'])


class AddTagForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=3,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Add new tag here'}))
    def save(self):
        Tag.objects.create(title=self.cleaned_data['title'])


class CategoryDeleteForm(forms.ModelForm):
    class Meta : 
        model = Category
        fields = []

class EditCategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=255,min_length=3,
                        widget= forms.TextInput
                        (attrs={'placeholder':'Add new name here'}))
    class Meta : 
        model = Category
        fields = ['title']


class TagDeleteForm(forms.ModelForm):
    class Meta : 
        model = Tag
        fields = []

class EditTagForm(forms.ModelForm):
    title = forms.CharField(max_length=255,min_length=3,
                        widget= forms.TextInput
                        (attrs={'placeholder':'Add new name here'}))
    class Meta : 
        model = Tag
        fields = ['title']


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,min_length=3,
#                            widget= forms.TextInput
#                            (attrs={'placeholder':'Add new post here'}))

#     def save(self):
#         Post.objects.create(title=self.cleaned_data['title'])


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostDeleteForm(forms.ModelForm):
    class Meta : 
        model = Post
        fields = []

class EditPostForm(forms.ModelForm):
    class Meta : 
        model = Post
        fields = ['title', 'short_description', 'descrption', 'status']
