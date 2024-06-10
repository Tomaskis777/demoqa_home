from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa

def test_check_icon(browser):
    # browser.get('https://www.maxidom.ru/')
    #
    # input = browser.find_element(By.NAME, 'USER_PHONE')
    #
    # if input is None:
    #     print('Не найден')
    # else:
    #     print('Найден')

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()