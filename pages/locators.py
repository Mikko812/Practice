# Локаторы для авторизации
class AuthLocators:
    LOGIN = '//a[contains(@href, "login.tmall.ru")]'   # xpath
    AUTH_EMAIL = 'fm-login-id'  # id
    AUTH_PASS = 'fm-login-password'  # id
    AUTH_BTN = 'fm-button.fm-submit.password-login'  # class
    LK_IN = '//span[@class="account-name"]/b'   # xpath


# Локаторы шапки страницы
class AlwaysOnPage:
    LOGO = 'div.site-logo a[href]'   # css
    BASKET = '//span[@class="text hidden-sm" and contains(text(), "Корзина")]'   # xpath
    FAVORITE = '//span[@class="text hidden-sm" and contains(text(), "Избранное")]'  # xpath
    CHAT = 'div.header-chat a'   # css
    HOME_PAGE = '//div[@class="mall-home"]'   # xpath
    ELECTRONICS = '//div[@class="channel" and @data-spm="3c-channel"]'   # xpath
    TEXNIKA = '//div[@class="channel" and @data-spm="fashion-channel"]'  # xpath
    DOMSAD = '//div[@class="channel" and @data-spm="uhod-channel"]'  # xpath
    MAMA = '//div[@class="channel" and @data-spm="muyin-channel"]'  # xpath
    MODA = '//div[@class="channel" and @data-spm="remont-channel"]'  # xpath
    ABOUT = '//div[@class="service hidden-md"]/a[contains(text(),"O Tmall")]'  # xpath
    DOSTAVKA = '//div[@class="service hidden-md"]/a[contains(text(),"Доставка")]'  # xpath
    GARANTII = '//div[@class="service"]/a[contains(text(), "Гарантии")]'  # xpath


# Локаторы поиска, Избранного и Корзины
class SearchAndBuy:
    MALL_HOME = '//div[@class="mall-home"]/a'  # xpath
    SEARCH = 'search-key'   # id
    SEARCH_BTN = 'input.search-button'   # css
    WISH_LIST = 'div.add-to-wishlist'   # css
    BUY_NUMBERS_BEFORE = 'nav-cart-num'  # id
    BUY_NUMBERS_AFTER = 'h2'  # tag
    BUY_CHECK = '//input[@class="next-checkbox-input"]'
    BASKET = '//span[@class="text hidden-sm" and contains(text(), "Корзина")]'   # xpath
    FAVORITE = '//span[@class="text hidden-sm" and contains(text(), "Избранное")]'  # xpath
    ADD_TO_FAVORITE = 'add-to-wishlist'   # class
    IN_FAVORITE = 'h3 a'   # css
    SEARCH_RESULT = '//strong[@class="active"]'  # xpath
    SEARCH_PHOTO = 'a.picRind.history-item '   # css
    SEARCH_LINK = 'a.history-item.product '   # css
    SKU_ITEM = '//li[@class="sku-property-item selected"]/div[@class="sku-property-image"]/img'   # xpath
    SKU_TITLE = 'div.sku-property-image img'   # css
    SKU_PROPERTY = 'sku-property'   # class
    ADD_CART = 'button.next-btn.next-large.next-btn-primary.addcart'   # css
    GO_BASKET = 'button.next-btn.next-small.next-btn-primary.view-shopcart'   # css
    TOTAL_PRICE = 'div.total-price dl dd'   # css
    DELETE = '//button[@ae_button_type="remove"]'   # xpath
    OK_DELETE = '//button[contains(text(), "OK")]'  # xpath
    REMOVE = 'a.remove'   # css


# Локаторы поиска
class SearchSort:
    SEARCH = 'search-key'   # id
    SEARCH_BTN = 'input.search-button'   # css
    GOODS_NAME = 'a.history-item.product '   # css
    BRANDS = 'li.brand-content  a'  # css
    BRAND_TITLE = '//li[@class="brand-content "]/a'  # xpath
    SEARCH_LINKS = 'a.history-item.product '  # css
    WRONG_ITEM = 'item'   # class
    SALE = 'linkOnSale'   # id
    DISCOUNT = 'div.price.price-m span'  # xpath
    PRICE_MIN = 'filter-price-from'   # id
    PRICE_MAX = 'filter-price-to'  # id
    PRICE_SUBMIT = 'filter-submit'  # id
    PRICE = '//div[@class="price price-m"]/span[@itemprop="price"]'  # xpath
    SORT_ZAKAZ = 'number_of_orders_1'  # id
    NUMS_ZAKAZ = 'em'  # css
    PRICE_LOW = 'price_lowest_1'  # id
    PRICE_HIGH = 'price_highest_1'  # id

# локаторы для поиска по параметрам
class Search:
    SEARCH = 'search-key'   # id
    SEARCH_BTN = 'input.search-button'   # css
    GOOD_PARAMS = 'ul.common-select.clearfix.one-row li a'   # css
    CATEGORIES = 'div.categories-entrance a.categories-title'   # css
    ELECTRONICA = '//span[contains(text(), "Электроника")]'   # xpath
    TV = '//dl[@class="sub-cate-items" and @data-key="tmallelectronics-tv"]/dt/a'   # xpath
    PARAM_NAMES = 'div.list-box-and-multiple-select dt.cate-title.attr-less'   # css
    PARAMS = 'ul.common-select.clearfix.one-row'   # css
    GOODS_LINKS = 'a.product '   # css
    PROPERTY_TITLES = 'span.property-title'   # css
    PROPERTY_VALUES = 'span.property-desc.line-limit-length'   # css
    GOOD_INFO = 'div.detail-extend-tab'   # css
    PROPERTY_TYPE = 'div.normaltwobuttoncontent'   # css
