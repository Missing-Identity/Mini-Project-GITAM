from django import forms
from django.contrib.auth.models import User
from health_app import models

# FORMS

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')
        def save(self, commit=True):
            user = super(UserForm, self).save(commit=False)
            if commit:
                user.save()
                return user

class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('title', 'text', 'post_pic')
