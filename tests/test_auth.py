from pages.auth_page import AuthPage, AuthPageCook
from pages.settings import email, password
from pages.functions import auth_assertions
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()


def test_tmall_auth_page():
    page = AuthPage(driver)
    page.login.click()
    login_page = page.get_current_url()
    assert 'login.aliexpress.com' in login_page, 'Не удалось перейти на страницу входа в ЛК.'
    page.email = email
    page.password = password
    page.auth_btn.click()
    page.wait_page_loaded()
    acc_name = page.lk_in.get_attribute('innerText')
    auth_assertions(acc_name, email.split('@')[0])


def test_tmall_auth_page_with_cookies():
    page = AuthPageCook(driver)
    acc_name = page.lk_in.get_attribute('innerText')
    auth_assertions(acc_name, email.split('@')[0])
