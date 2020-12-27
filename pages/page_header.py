from .locators import AlwaysOnPage
from .settings import start_url
from .elements import WebElement
from .base import WebPage
from .functions import tmall_auth_page


class PageHeader(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

    logo = WebElement(css_selector=AlwaysOnPage.LOGO)   # лого для перехода на главную
    basket = WebElement(xpath=AlwaysOnPage.BASKET)   # корзина покупок
    favorite = WebElement(xpath=AlwaysOnPage.FAVORITE)   # избранное
    chat = WebElement(css_selector=AlwaysOnPage.CHAT)   # онлайн-чат
    home_page = WebElement(xpath=AlwaysOnPage.HOME_PAGE)   # главная страница
    electronics = WebElement(xpath=AlwaysOnPage.ELECTRONICS)   # страница электроники
    texnika = WebElement(xpath=AlwaysOnPage.TEXNIKA)  # страница бытовой техники
    domsad = WebElement(xpath=AlwaysOnPage.DOMSAD)  # страница дом и сад
    mama = WebElement(xpath=AlwaysOnPage.MAMA)  # страница детям и мамам
    moda = WebElement(xpath=AlwaysOnPage.MODA)  # страница мода
    about = WebElement(xpath=AlwaysOnPage.ABOUT)  # страница O Tmall
    dostavka = WebElement(xpath=AlwaysOnPage.DOSTAVKA)  # страница доставки
    garantii = WebElement(xpath=AlwaysOnPage.GARANTII)  # страница гарантии

    def authorization(self, web_driver):
        page = tmall_auth_page(web_driver)
        return page
