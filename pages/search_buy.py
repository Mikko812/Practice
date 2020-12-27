from .locators import SearchAndBuy
from .settings import start_url
from .elements import WebElement
from .elements import ManyWebElements
from .base import WebPage
from .functions import tmall_auth_page
import pickle


class PageSearchBuyCook(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

        with open('tmall_cookies.pkl', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                web_driver.add_cookie(cookie)
        web_driver.refresh()

    mall_home = WebElement(xpath=SearchAndBuy.MALL_HOME)   # главная страница
    wish_list = WebElement(css_selector=SearchAndBuy.WISH_LIST)   # ссылка добавить в Избранное
    search = WebElement(id=SearchAndBuy.SEARCH)   # поле поиска
    search_btn = WebElement(css_selector=SearchAndBuy.SEARCH_BTN)   # кнопка поиска
    search_result = WebElement(xpath=SearchAndBuy.SEARCH_RESULT)   # результаты поиска
    buy_nums_before = WebElement(id=SearchAndBuy.BUY_NUMBERS_BEFORE)   # количество товаров в Корзине до покупки
    buy_nums_after = WebElement(tag_name=SearchAndBuy.BUY_NUMBERS_AFTER)  # количество товаров в Корзине после покупки
    search_photo = WebElement(css_selector=SearchAndBuy.SEARCH_PHOTO)  # фото товара в результатах поиска
    search_link = WebElement(css_selector=SearchAndBuy.SEARCH_LINK)  # ссылка на товар в результатах поиска
    sku_item = WebElement(xpath=SearchAndBuy.SKU_ITEM)  # характеристика товара (чтобы добавить в Корзину)
    sku_title = WebElement(css_selector=SearchAndBuy.SKU_TITLE)  # атрибут товара
    sku_property = ManyWebElements(class_name=SearchAndBuy.SKU_PROPERTY)   # свойства выбранного товара
    add_cart = WebElement(css_selector=SearchAndBuy.ADD_CART)  # добавить в Корзину
    go_basket = WebElement(css_selector=SearchAndBuy.GO_BASKET)  # перейти в Корзину
    buy_check = ManyWebElements(xpath=SearchAndBuy.BUY_CHECK)   # чекнуть последнюю покупку в Корзине
    total_price = WebElement(css_selector=SearchAndBuy.TOTAL_PRICE)   # к оплате
    favorite = WebElement(xpath=SearchAndBuy.FAVORITE)  # избранное
    add_to_favorite = WebElement(class_name=SearchAndBuy.ADD_TO_FAVORITE)   # добавить в Избранное
    in_favorite = WebElement(css_selector=SearchAndBuy.IN_FAVORITE)  # ссылка на товар в Избранном
    delete = WebElement(id=SearchAndBuy.DELETE)   # удалить из Корзины
    ok_delete = WebElement(xpath=SearchAndBuy.OK_DELETE)  # OK удалить из Корзины
    remove = WebElement(css_selector=SearchAndBuy.REMOVE)  # удалить из Избранного


class PageSearchBuy(WebPage):
    def __init__(self, web_driver, url=start_url):
        super().__init__(web_driver, url)

    mall_home = WebElement(xpath=SearchAndBuy.MALL_HOME)   # главная страница
    wish_list = WebElement(css_selector=SearchAndBuy.WISH_LIST)   # ссылка добавить в Избранное
    search = WebElement(id=SearchAndBuy.SEARCH)   # поле поиска
    search_btn = WebElement(css_selector=SearchAndBuy.SEARCH_BTN)   # кнопка поиска
    search_result = WebElement(xpath=SearchAndBuy.SEARCH_RESULT)   # результаты поиска
    buy_nums_before = WebElement(id=SearchAndBuy.BUY_NUMBERS_BEFORE)   # количество товаров в Корзине до покупки
    buy_nums_after = WebElement(tag_name=SearchAndBuy.BUY_NUMBERS_AFTER)  # количество товаров в Корзине после покупки
    search_photo = WebElement(css_selector=SearchAndBuy.SEARCH_PHOTO)  # фото товара в результатах поиска
    search_link = WebElement(css_selector=SearchAndBuy.SEARCH_LINK)  # ссылка на товар в результатах поиска
    sku_item = WebElement(xpath=SearchAndBuy.SKU_ITEM)  # характеристика товара (чтобы добавить в Корзину)
    sku_title = WebElement(css_selector=SearchAndBuy.SKU_TITLE)  # атрибут товара
    sku_property = ManyWebElements(class_name=SearchAndBuy.SKU_PROPERTY)   # свойства выбранного товара
    add_cart = WebElement(css_selector=SearchAndBuy.ADD_CART)  # добавить в Корзину
    go_basket = WebElement(css_selector=SearchAndBuy.GO_BASKET)  # перейти в Корзину
    buy_check = ManyWebElements(xpath=SearchAndBuy.BUY_CHECK)   # чекнуть последнюю покупку в Корзине
    total_price = WebElement(css_selector=SearchAndBuy.TOTAL_PRICE)   # к оплате
    favorite = WebElement(xpath=SearchAndBuy.FAVORITE)  # избранное
    add_to_favorite = WebElement(class_name=SearchAndBuy.ADD_TO_FAVORITE)   # добавить в Избранное
    in_favorite = WebElement(css_selector=SearchAndBuy.IN_FAVORITE)  # ссылка на товар в Избранном
    delete = WebElement(xpath=SearchAndBuy.DELETE)   # удалить из Корзины
    ok_delete = WebElement(xpath=SearchAndBuy.OK_DELETE)  # OK удалить из Корзины
    remove = WebElement(css_selector=SearchAndBuy.REMOVE)  # удалить из Избранного

    def authorization(self, web_driver):
        page = tmall_auth_page(web_driver)
        return page
