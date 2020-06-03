# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setup(self):
        Post.objects.create(title = 'sample')
        Post.objects.create(text = 'just a text')

    def text_object(self):
        post = Post.get.object(id = 1)
        expected_title_name = f'{post.title}'
        expected_post_name = f'{post.text}'
        self.assertEqual(expected_title_name, 'sample')
        self.assertEqual(expected_post_name, 'just a text')
