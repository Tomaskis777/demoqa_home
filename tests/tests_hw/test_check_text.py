# from selenium import webdriver
# import pytest
#
# class Components:
#
#     def get_text(self):
#         str(self.find_element('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.').text)
#         if str == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
#             return True
#         else:
#             return False
#
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
# def test_get_title(driver):
#     driver.get("https://demoqa.com/")
#
# def click_on_the_btn(self):
#     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()
#
# def get_text(self):
#     str(self.find_element('Please select an item from left to start practice.').text)
#     if str == 'Please select an item from left to start practice.':
#         return True
#     else:
#         return False

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestCheckText(unittest.TestCase):

    def get_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#app > footer').text

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_text_in_footer(self):
        # Перейти на страницу 'https://demoqa.com/'
        driver = self.driver
        driver.get("https://demoqa.com/")

        # Проверить текст в подвале
        footer_text = self.driver.find_element(By.CSS_SELECTOR, '#app > footer').text
        expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
        self.assertEqual(footer_text, expected_text)

    # Метод tearDown() для закрытия браузера после теста
    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_text_in_footer(self):
        # Перейти на страницу 'https://demoqa.com/'
        driver = self.driver
        driver.get("https://demoqa.com/elements/")

        # Проверить текст в подвале
        footer_text = self.driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > div.col-12.mt-4.col-md-6').text
        expected_text = "Please select an item from left to start practice."
        self.assertEqual(footer_text, expected_text)

    # Метод tearDown() для закрытия браузера после теста
    def tearDown(self):
        self.driver.quit()
