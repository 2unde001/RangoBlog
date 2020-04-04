from django.test import TestCase
from .models import Post

# Create your tests here.
class HomePageViewTest(TestCase):
    def setUp(self):
        self.user = Post.objects.get_or_create(
            username="testname", email="testemail", password="testpassword"
        )

        self.post = Post.objects.create(
            tittle="Django Project", author=self.user, body="blog contents 34"
        )

        def test_string_representation(self):
            post = Post(tittle="blog title")
            self.assertEqual(str(post), post.tittle)
