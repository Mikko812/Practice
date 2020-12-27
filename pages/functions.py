from pages.auth_page import AuthPage
from pages.settings import email, password


# словарь параметров для test_page_header {название теста: (часть адреса страницы, пункт строки меню)}
links = {'about': ('service-header', 'O Tmall'), 'dostavka': ('delivery', 'Доставка'), 'chat': ('portal', 'Онлайн-чат'),
         'garantii': ('guarantee_service', 'Гарантии'), 'basket': ('shopcart', 'Корзина'),
         'favorite': ('wishlist', 'Избранное'), 'elektonika': ('3c_electronics', 'Электроника'),
         'texnika': ('sda_appliances', 'Бытовая техника'), 'domsad': ('home_and_garden', 'Дом и Сад'),
         'mama': ('mall_kids', 'Детям и Мамам'), 'moda': ('mall_fashion', 'Мода'), 'logo': ('tmall.ru/?spm', 'Главная')}


def tmall_auth_page(driver):
    page = AuthPage(driver)
    page.login.click()
    page.email = email
    page.password = password
    page.auth_btn.click()
    page.wait_page_loaded()
    return page


def header_assertions(test_obj: str, curr_page: str):  # для test_sheader
    try:
        assert links[test_obj][0] in curr_page
        msg = f'\033[32mПереход на страницу \"{links[test_obj][1]}\" подтвержден!\033[0m'
    except AssertionError:
        msg = f'\033[31mОшибка перехода на страницу \"{links[test_obj][1]}\"!\033[0m'
    print(msg)


def auth_assertions(acc_name: str, name: str):  # для test_auth
    try:
        assert acc_name == name
        msg = f'\033[32mАвторизация прошла успешно!\033[0m'
    except AssertionError:
        msg = '\033[31mНе удалось войти в Личный Кабинет!\033[0m'
    print('\n', msg)


def search_buy_assertions(param1: str, param2: str, msg: str, equal=1):  # для test_search_buy
    if equal:
        try:
            assert param1 == param2
            msg = f'\033[32mТЕСТ \"{msg}\" ПРОЙДЕН!\033[0m'
        except AssertionError:
            msg = f'\033[31mТЕСТ \"{msg}\" НЕ ПРОЙДЕН!\033[0m'
    else:
        try:
            assert param1 != param2
            msg = f'\033[32mТЕСТ \"{msg}\" ПРОЙДЕН!\033[0m'
        except AssertionError:
            msg = f'\033[31mТЕСТ \"{msg}\" НЕ ПРОЙДЕН!\033[0m'
    print('\n', msg)


def check_scope(min_pr: float, max_pr: float, all_prices: list) -> list:  # для test_search_sort
    index_prices = [x for x in range(len(all_prices))]
    index_prices = list(filter(lambda x: ' - ' not in all_prices[x], index_prices))
    all_prices = list(filter(lambda x: ' - ' not in x, all_prices))  # удаляем цены, указанные как 'цена1 - цена2'
    all_prices = list(map(lambda x: float(x[:-5].replace(',', '.').replace(' ', '')), all_prices))  # переводим во float
    ret = []
    for i in range(len(all_prices)):
        if all_prices[i] < min_pr or all_prices[i] > max_pr:
            ret.append(i)
    return ret


def check_sort(list_to_check, sort_type='price', sort_order='ascending'):  # для test_search_sort
    index_prices = [x for x in range(len(list_to_check))]
    if sort_type == 'price':
        index_prices = list(filter(lambda x: ' - ' not in list_to_check[x], index_prices))
        list_to_check = list(filter(lambda x: ' - ' not in x, list_to_check))  # удаляем цены, указанные как 'цена1 - цена2'
        list_to_check = list(map(lambda x: float(x[:-5].replace(',', '.').replace(' ', '')), list_to_check))  # переводим во float
    ret = []
    if sort_order == 'ascending':   # порядок сортировки по возрастанию
        for i in range(1, len(list_to_check)):
            if list_to_check[i] < list_to_check[i-1]:
                ret.append(index_prices[i])
    else:   # порядок сортировки по убыванию
        for i in range(1, len(list_to_check)):
            if list_to_check[i] > list_to_check[i-1]:
                ret.append(index_prices[i])
    return ret


def name_correct(name: str) -> str:  # для test_search
    if '[' in name:
        return name.split(' [')[0]
    elif '(' in name:
        return name.split(' (')[0]
    elif len(name.split(' ')) > 5:
        name = name.split(' ')[:5]
        return ' '.join(name)
    else:
        return name

def assertion_properties(params: list, props_list: list, name: str):  # для test_search
    try:
        assert params in props_list
        print(f'\033[32mТЕСТ проверки наличия характеристики \'{params[0]} = {params[1]}\' '
              f'у товара \'{name}\' прошел УСПЕШНО!\033[0m')
    except AssertionError:
        print(f'\033[31mУ товара \'{name}\' нет выбранной характеристики \'{params[0]} = {params[1]}\' '
              f'или она не соответствует запросу!\033[0m')
