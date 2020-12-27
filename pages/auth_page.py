from .locators import AuthLocators
from .settings import start_url
from .elements import WebElement
from .base import WebPage
import pickle


class AuthPage(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

    login = WebElement(xpath=AuthLocators.LOGIN)   # поле логина
    email = WebElement(id=AuthLocators.AUTH_EMAIL)   # эл. почта для логина
    password = WebElement(id=AuthLocators.AUTH_PASS)   # пароль
    auth_btn = WebElement(class_name=AuthLocators.AUTH_BTN)   # кнопка Войти
    lk_in = WebElement(xpath=AuthLocators.LK_IN)   # имя пользователя


class AuthPageCook(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

        with open('tmall_cookies.pkl', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                web_driver.add_cookie(cookie)
        web_driver.refresh()

    lk_in = WebElement(xpath=AuthLocators.LK_IN)
