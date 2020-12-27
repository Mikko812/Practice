from .locators import SearchSort
from .settings import start_url
from .elements import WebElement
from .elements import ManyWebElements
from .base import WebPage


class PageSearchSort(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

    search = WebElement(id=SearchSort.SEARCH)   # поле поиска
    search_btn = WebElement(css_selector=SearchSort.SEARCH_BTN)   # кнопка поиска
    goods_name = ManyWebElements(css_selector=SearchSort.GOODS_NAME)   # названия товаров
    brands = ManyWebElements(css_selector=SearchSort.BRANDS)   # логотипы брендов
    brand_title = ManyWebElements(xpath=SearchSort.BRAND_TITLE)   # названия брендов
    search_links = ManyWebElements(css_selector=SearchSort.SEARCH_LINKS)   # ссылки на товары
    wrong_item = ManyWebElements(class_name=SearchSort.WRONG_ITEM)   # элемент для скриншота
    sale = WebElement(id=SearchSort.SALE)   # товар со скидкой
    discount = ManyWebElements(css_selector=SearchSort.DISCOUNT)   # цена товара
    price_min = WebElement(id=SearchSort.PRICE_MIN)   # минимальная цена товара для поиска
    price_max = WebElement(id=SearchSort.PRICE_MAX)   # максимальная цена товара для поиска
    price_submit = WebElement(id=SearchSort.PRICE_SUBMIT)   # ОК для поиска в диапазоне цен
    price = ManyWebElements(xpath=SearchSort.PRICE)   # цена товара
    sort_zakaz = WebElement(id=SearchSort.SORT_ZAKAZ)   # элемент с количеством заказов
    nums_zakaz = ManyWebElements(css_selector=SearchSort.NUMS_ZAKAZ)   # количество заказов
    price_low = WebElement(id=SearchSort.PRICE_LOW)   # сортировка по возрастанию
    price_high = WebElement(id=SearchSort.PRICE_HIGH)   # сортировка по убыванию
