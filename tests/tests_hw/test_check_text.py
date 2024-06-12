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
#     title_element = driver.find_element_by_tag_name("© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.").text
#     text = title_element.text
#     assert text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."  # Текст элемента совпадает с атрибутом innerHTML
