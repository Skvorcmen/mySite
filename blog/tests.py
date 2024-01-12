from django.urls import resolve
from django.test import TestCase
from blog.views import home_page, article_page
from blog.models import Article
from django.http import HttpRequest
# from django.core.files import File
# from django.test import TestCase
from django.urls import reverse
from datetime import datetime
import pytz


class ArticlePageTest(TestCase):
    def test_article_page_displays_correct_articles(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full text 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='ooo-lya-lya'
        )

        request = HttpRequest()
        response = article_page(request, 'ooo-lya-lya')
        html = response.content.decode('utf8')

        self.assertIn("title 1", html)
        self.assertIn("full text 1", html)
        self.assertNotIn("summary 1", html)


class HomePageTest(TestCase):

    def test_home_page_display_articles(self):
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full text 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug 1'
        )

        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full text 2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug 2'
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn("title 1", html)
        self.assertIn("/blog/slug 1", html)
        self.assertNotIn("full text 1", html)

        self.assertIn("title 2", html)
        self.assertIn("/blog/slug 2", html)
        self.assertNotIn("full text 2", html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        url = reverse('home_page')
        response = self.client.get(url)
        # request = HttpRequest()
        # response = home_page(request)
        self.assertTemplateUsed(response, 'home_page.html')
        # html = response.content.decode("utf8")
        # self.assertTrue(html.startswith("<html>"))
        # self.assertIn("<title>Сайт Василия Скворцова</title>", html)
        # self.assertIn("<h1>Василий Скворцов</h1>", html)
        # self.assertTrue(html.endswith('</html>'))


class ArticleModelTest(TestCase):
    def test_article_model_save_and_retrieve(self):
        article1 = Article(
            title='article 1',
            full_text='full_test 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug=1'
        )
        article1.save()

        article2 = Article(
            title='article 2',
            full_text='full_test 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug=2'
        )
        article2.save()

        all_articles = Article.objects.all()

        self.assertEqual(len(all_articles), 2)

        self.assertEqual(
            all_articles[0].title,
            article1.title
        )

        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )

        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )
