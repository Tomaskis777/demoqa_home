from selenium.webdriver.common.by import By


def test_check_icon(browser):
    icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')

    if icon is None:
        print('Не найден')
    else:
        print('Найден')