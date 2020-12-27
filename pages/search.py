from .locators import Search
from .settings import start_url
from .elements import WebElement
from .elements import ManyWebElements
from .base import WebPage


class PageSearch(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

    search = WebElement(id=Search.SEARCH)   # поле поиска
    search_btn = WebElement(css_selector=Search.SEARCH_BTN)   # кнопка поиска
    good_params = ManyWebElements(css_selector=Search.GOOD_PARAMS)   # характеристики товара
    categories = WebElement(css_selector=Search.CATEGORIES)   # категории товаров
    electronica = WebElement(xpath=Search.ELECTRONICA)   # раздел Электроника
    tv = WebElement(xpath=Search.TV)   # телевизоры
    param_names = ManyWebElements(css_selector=Search.PARAM_NAMES)   # названия характеристик товара
    params = ManyWebElements(css_selector=Search.PARAMS)   # значения характеристик товара
    goods_links = ManyWebElements(css_selector=Search.GOODS_LINKS)   # ссылки на товары
    property_titles = ManyWebElements(css_selector=Search.PROPERTY_TITLES)   # параметры товара
    property_values = ManyWebElements(css_selector=Search.PROPERTY_VALUES)   # значения параметров товара
    good_info = WebElement(css_selector=Search.GOOD_INFO)   # инфо о товаре для scroll_to_element
    property_type = WebElement(css_selector=Search.PROPERTY_TYPE)   # кнопка проверяемого параметра
