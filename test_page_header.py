from pages.page_header import PageHeader
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# тестирование Заголовка страницы (Корзина, Избранное, Ссылки на группы товаров, Лого)
def test_page_header():
    print('\n')
    page = PageHeader(driver)
    page.authorization(driver)
    page.about.click()
    curr_page = page.get_current_url()
    assert 'service-header' in curr_page, 'Ошибка перехода на страницу O Tmall!'
    page.go_back()
    page.dostavka.click()
    curr_page = page.get_current_url()
    assert 'delivery' in curr_page, 'Ошибка перехода на страницу Доставка!'
    page.go_back()
    page.garantii.click()
    curr_page = page.get_current_url()
    assert 'guarantee_service' in curr_page, 'Ошибка перехода на страницу Гарантии!'
    page.go_back()
    page.basket.click()   # переход в Корзину покупок
    curr_page = page.get_current_url()
    assert 'shopcart' in curr_page, 'Ошибка перехода на страницу Корзина!'
    page.go_back()
    page.favorite.click()   # переход в Избранное
    curr_page = page.get_current_url()
    assert 'wishlist' in curr_page, 'Ошибка перехода на страницу Избранное!'
    page.go_back()
    page.electronics.click()
    curr_page = page.get_current_url()
    assert '3c_electronics' in curr_page, 'Ошибка перехода на страницу Электроника!'
    page.texnika.click()
    curr_page = page.get_current_url()
    assert 'sda_appliances' in curr_page, 'Ошибка перехода на страницу Бытовая техника!'
    page.domsad.click()
    curr_page = page.get_current_url()
    assert 'home_and_garden' in curr_page, 'Ошибка перехода на страницу Дом и Сад!'
    page.mama.click()
    curr_page = page.get_current_url()
    assert 'mall_kids' in curr_page, 'Ошибка перехода на страницу Детям и Мамам!'
    page.moda.click()
    curr_page = page.get_current_url()
    assert 'mall_fashion' in curr_page, 'Ошибка перехода на страницу Мода!'
    page.logo.click()
    curr_page = page.get_current_url()
    assert 'tmall.ru/?spm' in curr_page, 'Ошибка перехода на страницу Главная!'


def test_about(page=None):
    if not page:   #тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.about.click()
    curr_page = page.get_current_url()
    assert 'service-header' in curr_page, '\nОшибка перехода на страницу O Tmall!'
    page.go_back()

def test_dostavka(page=None):
    if not page:   #тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.dostavka.click()
    curr_page = page.get_current_url()
    assert 'delivery' in curr_page, 'Ошибка перехода на страницу Доставка!'
    page.go_back()

def test_garantii(page=None):
    if not page:   #тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.garantii.click()
    curr_page = page.get_current_url()
    assert 'guarantee_service' in curr_page, 'Ошибка перехода на страницу Гарантии!'
    page.go_back()

def test_shopcart(page=None):
    if not page:   #тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.basket.click()   # переход в Корзину покупок
    curr_page = page.get_current_url()
    assert 'shopcart' in curr_page, 'Ошибка перехода на страницу Корзина!'
    page.go_back()

def test_header():   # общий тест всех тестов шапки сайта
    page = PageHeader(driver)
    page.authorization(driver)
    test_shopcart(page)
    test_about(page)
    test_dostavka(page)
    test_garantii(page)
