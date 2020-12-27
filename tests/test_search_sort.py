from pages.search_sort import PageSearchSort
from selenium import webdriver
from pages.functions import check_sort, check_scope
import random
import inspect
driver = webdriver.Chrome()
driver.maximize_window()


def make_screenshot(page, test, index):
    wrong_element = page.wrong_item[index]
    driver.execute_script("arguments[0].scrollIntoView();", wrong_element)
    driver.execute_script("arguments[0].style.border='3px solid red'", wrong_element)
    driver.save_screenshot(f'../screenshots/TEST {test} - SS{index}.png')
    driver.execute_script("arguments[0].style.border='0px'", wrong_element)


def assertion_handler_sort(page, test='', errors_list=[], req=''):
    if errors_list != []:   # в выдаче поиска не все товары соответствуют запросу
        print('\n', f'\033[31mВ выдаче теста <{test}> не все товары соответствуют запросу <{req}>!\033[0m'
              '\nСкриншоты этих товаров записаны в папку screenshots.')
        for index in errors_list:
            make_screenshot(page, test, index)
    else:
        print('\n', f'\033[32mТЕСТ <{test}> С ЗАПРОСОМ <{req}> ПРОЙДЕН УСПЕШНО!\033[0m')


# поиск по слову
def test_search_goods_numbers():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    goods = page.goods_name.count()
    try:
        assert goods <= 48
        print('\n', '\033[32mКоличество товаров на странице не превышает 48!\033[0m')
    except AssertionError:
        print('\n', '\033[31mКоличество товаров на странице больше 48!\033[0m')


# поиск по брендам
def test_search_by_brand():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    nums = page.brands.count()
    driver.execute_script('document.querySelector("#brandWallSpanViewmore.brands-wall-viewmore.more").click()')
# Чтобы не увеличивать время тестов, тестируем соответствие выдачи поиска по бренду по одному, но выбранному случайно.
# При реальном тестировании, естественно, используем цикл for для списка всех брендов.
    index = random.randint(0, nums - 1)
    brand_title_list = page.brand_title.get_attribute('outerHTML')   # список брендов
    brand_title_list = list(map(lambda x: x.split('title=\" ')[1].split('\"')[0], brand_title_list))
    page.brands[index].click()   # клик по случайно выбранному бренду
    page.wait_page_loaded()
    goods_titles = page.search_links.get_text()   # текст ссылки на товар
    curr_brand = brand_title_list[index].lower()
    search_result = [x for x in range(len(goods_titles)) if curr_brand not in goods_titles[x].lower()]
# в search_result индексы товаров, бренды которых не являются заданными в запросе
    test = inspect.stack()[0][3][5:]
    assertion_handler_sort(page, test, search_result, curr_brand)


# поиск товаров со скидкой
def test_search_sale():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    page.sale.click()
    page.wait_page_loaded()
    prices = page.discount
    prices = list(filter(lambda x: 'value' in x.get_attribute('className'), prices))
    search_result = list(filter(lambda x: prices[x].get_attribute('className') == 'value', range(len(prices))))
# в search_result индексы товаров, у которых нет скидки
    test = inspect.stack()[0][3][5:]
    msg = 'поиск товаров со скидкой'
    assertion_handler_sort(page, test, search_result, msg)


# поиск в диапазоне цен
def test_search_price_scope():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    min_price = '12000'
    page.price_min.send_keys(min_price)
    max_price = '20000'
    page.price_max.send_keys(max_price)
    page.price_submit.click()
    all_prices = page.price.get_text()
    search_result = check_scope(int(min_price), int(max_price), all_prices)
# в search_result индексы товаров, цены на которые находятся вне заданного диапазона
    test = inspect.stack()[0][3][5:]
    msg = 'поиск товаров в диапазоне цен'
    assertion_handler_sort(page, test, search_result, msg)


# сортировка по количеству заказов
def test_sort_zakaz():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    page.sort_zakaz.click()
    zakazy = page.nums_zakaz.get_text()
    zakazy = list(map(lambda x: int(x.replace(')', '').replace('По заказам (', '').replace('Заказ (', '')), zakazy))
    search_result = check_sort(zakazy, 'zakaz', 'descending')
# в search_result индексы товаров, которые отсортированы неправильно
    test = inspect.stack()[0][3][5:]
    msg = 'cортировка по количеству заказов'
    assertion_handler_sort(page, test, search_result, msg)


# сортировка по ценам по возрастанию
def test_sort_price_low_to_high():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    page.price_low.click()
    all_prices = page.price.get_text()
    search_result = check_sort(all_prices, 'price', 'ascending')
# в search_result индексы товаров, которые отсортированы неправильно
    test = inspect.stack()[0][3][5:]
    msg = 'cортировка по возрастанию цены'
    assertion_handler_sort(page, test, search_result, msg)


# сортировка по ценам по убыванию
def test_sort_price_high_to_low():
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    page.price_low.click()
    page.price_high.click()
    all_prices = page.price.get_text()
    search_result = check_sort(all_prices, 'price', 'descending')
# в search_result индексы товаров, которые отсортированы неправильно
    test = inspect.stack()[0][3][5:]
    msg = 'cортировка по убыванию цены'
    assertion_handler_sort(page, test, search_result, msg)


def test_search_and_sort():
    test_search_goods_numbers()
    test_search_by_brand()
    test_search_sale()
    test_search_price_scope()
    test_sort_zakaz()
    test_sort_price_low_to_high()
    test_sort_price_high_to_low()
