from selenium import webdriver
from selenium.webdriver.common.by import By
# import unittest
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import pytz


class BasicInstallTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full text 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='ooo-lya-lya'
        )

    def test_home_page_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Сайт Василия Скворцова", self.browser.title)

    def test_home_page_header(self):
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Василий Скворцов", header)

        def test_layout_and_styling(self):
            self.browser.get(self.live_server_url)
            self.browser.set_window_size(1024, 768)

            header = self.browser.find_element(By.TAG_NAME, "h1")
            self.assertAlmosTrue(header.location["x"] > 10)

    def test_home_page_blog(self):
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        article_text = self.browser.find_element(
            By.CLASS_NAME,
            'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_text)

    def test_home_page_article_title_link_Leads_to_article_page(self):
        # открывает главную страницу
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        article_title_text = article_title.text
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute("href"))
        article_page_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        self.assertEqual(article_title_text, article_page_title.text)

    def tearDown(self):
        self.browser.quit()
