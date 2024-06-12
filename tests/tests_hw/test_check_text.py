from selenium import webdriver
import pytest

class Components:

    def get_text(self):
        str(self.find_element('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.').text)
        if str == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
            return True
        else:
            return False


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_get_title(driver):
    driver.get("https://demoqa.com/")

def click_on_the_btn(self):
    self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

def get_text(self):
    str(self.find_element('Please select an item from left to start practice.').text)
    if str == 'Please select an item from left to start practice.':
        return True
    else:
        return False
