from pages.page_header import PageHeader
from selenium import webdriver
from pages.functions import header_assertions
import inspect
driver = webdriver.Chrome()
driver.maximize_window()
print('\n')


# тестирование Заголовка страницы (Корзина, Избранное, Ссылки на группы товаров, Лого)
def test_about(page=None):
    if not page:   # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.about.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]   # получаем имя текущей функции без 'test_'
    header_assertions(test_obj, curr_page)
    page.go_back()


def test_dostavka(page=None):
    if not page:   # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.dostavka.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
    page.go_back()


def test_garantii(page=None):
    if not page:   # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.garantii.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
    page.go_back()


def test_chat(page=None):
    if not page:   # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    tmall = driver.current_window_handle
    page.chat.click()
    new_window = [w for w in driver.window_handles if w != tmall]
    driver.switch_to.window(new_window[0])
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
    driver.close()
    driver.switch_to.window(tmall)


def test_basket(page=None):
    if not page:   # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
        page.authorization(driver)
    page.basket.click()   # переход в Корзину покупок
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
    page.go_back()


def test_favorite(page=None):
    if not page:   # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
        page.authorization(driver)
    page.favorite.click()   # переход в Избранное
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
    page.go_back()


def test_elektonika(page=None):
    if not page:  # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.electronics.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_texnika(page=None):
    if not page:  # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.texnika.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_domsad(page=None):
    if not page:  # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.domsad.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_mama(page=None):
    if not page:  # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.mama.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_moda(page=None):
    if not page:  # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.moda.click()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_logo(page=None):
    if not page:  # тест запускается отдельно, не через test_header
        page = PageHeader(driver)
    page.logo.click()   # переход на Главную по клику на Лого
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


# СЦЕНАРИЙ: 1. Авторизация; 2. Переход по всем ссылкам "шапки" сайта
def test_header():
    page = PageHeader(driver)
    page.authorization(driver)
    test_basket(page)
    test_favorite(page)
    test_about(page)
    test_dostavka(page)
    test_garantii(page)
    test_chat(page)
    test_elektonika(page)
    test_texnika(page)
    test_domsad(page)
    test_mama(page)
    test_moda(page)
    test_logo(page)
