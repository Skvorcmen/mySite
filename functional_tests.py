from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class BasicInstallTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_home_page_title(self):
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn("Сайт Василия Скворцова", self.browser.title)

    def test_home_page_header(self):
        self.browser.get("http://127.0.0.1:8000")
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Василий Скворцов", header)

    def test_home_page_blog(self):
        self.browser.get("http://127.0.0.1:8000")
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get("http://127.0.0.1:8000")
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        article_text = self.browser.find_element(
            By.CLASS_NAME,
            'article-text')
        self.assertTrue(article_title)
        self.assertTrue(article_text)


    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

#        self.fail("Finish the test!")
 