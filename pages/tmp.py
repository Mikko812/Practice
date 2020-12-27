from selenium import webdriver
driver = webdriver.Chrome()
from pages.settings import start_url
import pickle


driver.get(start_url)
with open('../tests/tmall_cookies.pkl', 'wb') as cookies:
    pickle.dump(driver.get_cookies(), cookies)

chrome_options = Options()
chrome_options.add_argument("window-size=1600,800")
driver = webdriver.Chrome(chrome_options=chrome_options)

with open('../tests/tmall_cookies.pkl', 'rb') as cookiesfile:
    cookies = pickle.load(cookiesfile)
    for cookie in cookies:
        web_driver.add_cookie(cookie)
web_driver.refresh()


def test_search_addcart_favorite():
    print('\n')
    page = PageSearch(driver)
    page.authorization(driver)
    page.wait_page_loaded()
    buy_nums = int(page.buy_nums_before.get_attribute('innerText'))  # количество товаров в корзине до добавления товара
    page.search.send_keys('Смартфон')   # тестирование поиска
    page.search_btn.click()
    page.wait_page_loaded()
    for_assert = page.search_result.get_attribute('innerText')[1:-1]
    assert for_assert == 'smartphone', 'Поиск по слову "Смартфон" неуспешен'
    assert page.search_photo.is_clickable(), 'Ссылка-фото на страницу товара нерабочая!'
    assert page.search_link.is_clickable(), 'Ссылка на страницу товара нерабочая!'
    link_text = page.search_link.get_attribute('innerText')
    element = page.search_photo.find()
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    page.add_to_favorite.click()
    page.favorite.click()
    link_text_fav = page.in_favorite.get_attribute('innerText')
    assert link_text == link_text_fav, 'Товар не добавлен в Избранное'
    page.remove.click()
    page.go_back()
    page.go_back()
    page.search_link.click()
    page.wait_page_loaded()
    params_num = page.sku_property.find()
    if len(params_num) == 1:
        driver.execute_script("document.getElementsByClassName('next-btn next-large next-btn-primary addcart')[0].click();")
        page.go_basket.wait_to_be_clickable()
        page.go_basket.click()
        page.wait_page_loaded()
        # количество товаров в корзине после добавления товара
        buy_nums_new = int(page.buy_nums_after.get_attribute('innerText').split(' ')[1][1:-1])
        assert buy_nums + 1 == buy_nums_new, 'Количество покупок в Корзине не изменилось'
    else:
        driver.execute_script("document.getElementsByClassName('sku-property-item')[0].className = 'sku-property-item selected';")
        driver.execute_script("document.getElementsByClassName('sku-property-item selected')[0].click();")
        driver.execute_script("document.getElementsByClassName('next-btn next-large next-btn-primary addcart')[0].click();")
        page.go_basket.wait_to_be_clickable()
        page.go_basket.click()
        page.wait_page_loaded()
        buy_nums_new = int(page.buy_nums_after.get_attribute('innerText').split(' ')[1][1:-1])
        assert buy_nums + 1 == buy_nums_new, 'Количество покупок в Корзине не изменилось'
    price_before = page.total_price.get_text()
    print(price_before)
    page.buy_check.find()[2].click()
    time.sleep(2)
    price_after = page.total_price.get_attribute('innerText')
    assert price_before != price_after, 'Сумма к оплате не изменилась'
    page.delete.click()
    page.ok_delete.wait_to_be_clickable()
    page.ok_delete.click()


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



def my_screenshot(page, index):
    page = PageSearchSort(driver)
    page.search.send_keys('Смартфон')
    page.search_btn.click()
    page.wait_page_loaded()
    wrong_element = page.wrong_item[index]
    driver.execute_script("arguments[0].scrollIntoView();", wrong_element)
    driver.execute_script("arguments[0].style.border='3px solid red'", wrong_element)
    driver.save_screenshot(f'SS{index}.png')
    driver.execute_script("arguments[0].style.border='0px'", wrong_element)


try:
    assert params_list[i] in props_list
    print(params_list[i])
except AssertionError:
    print(f'У товара {page.goods_links[0].get_text()} нет выбранной характеристики {params_list[i][0]} = '
          f'{params_list[i][1]} или она не соответствует запросу!')