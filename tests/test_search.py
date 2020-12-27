from pages.search import PageSearch
from selenium import webdriver
from pages.functions import name_correct, assertion_properties
import random
import time
driver = webdriver.Chrome()
driver.maximize_window()


''' Тест поиска товара "Телевизоры" с заданными характеристиками
Сценарий: Выбираем "Телевизоры" -> выбираем 1-й параметр из списка (сделано для экономии времени,
в реальном тесте добавляем цикл for по всем параметрам) -> собираем все характеристики товара -> 
проверям наличие в них нашего параметра.'''


def test_search_by_properties():
    page = PageSearch(driver)
    page.categories.click()
    page.electronica.click()
    page.tv.click()
    param_names = page.param_names.get_text()   # названия характеристик товара
    params = page.params.get_attribute('innerText')   # названия параметров
    params = [x for x in params if '\t\t' not in x]
    params = [x.split('\n')[0] for x in params]
    params_list = [[a, b] for a, b in zip(param_names, params)]   # список ['характеристика', 'значение']
    print('\n')
    for i in range(len(param_names)):   # перебираем все характеристики товара
        driver.execute_script('list_params = document.querySelectorAll("div.list-box-and-multiple-select");'
                              f'list_params[{i}].querySelectorAll("dl dd ul li a")[0].click();')
        index = random.randint(0, page.goods_links.count() - 1)   # номер товара для проверки
        name = page.goods_links[index].get_attribute('innerText')   # название товара, выбранного для проверки
        name = name_correct(name)
        page.goods_links[index].click()  # берем случайный товар с заданными характеристиками
        page.wait_page_loaded()
        driver.execute_script('document.querySelector("#product-detail").scrollIntoView();')
        driver.execute_script('document.querySelectorAll("span.tab-inner-text")[2].click();')  # клик 'ХАРАКТЕРИСТИКИ'
        time.sleep(2)
        prop_titles = page.property_titles.get_text()   # названия характеристик
        prop_titles = [x[:-2] for x in prop_titles]
        prop_values = page.property_values.get_text()   # названия параметров
        props_list = [[a, b] for a, b in zip(prop_titles, prop_values)]   # список характеристик товара, выбранного для проверки
        assertion_properties(params_list[i], props_list, name)
        page.go_back()
        page.go_back()
        page.wait_page_loaded()
        if page.property_type.is_presented():   # удаляем последний параметр
            driver.execute_script('document.querySelector("a.remove-common-select-multiple").click();')
        page.wait_page_loaded()
