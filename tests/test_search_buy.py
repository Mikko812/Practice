from pages.search_buy import PageSearchBuyCook, PageSearchBuy
from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.functions import search_buy_assertions
import time
driver = webdriver.Chrome()
driver.maximize_window()


# тестирование поиска, добавления в Корзину и в Избранное, покупки товара
def test_search(page=None):
    if not page:  # тест запускается отдельно
        page = PageSearchBuy(driver)
    page.search.send_keys('Смартфон')  # тестирование поиска
    page.search_btn.click()
    page.wait_page_loaded()
    for_assert = page.search_result.get_attribute('innerText')[1:-1]
    search_buy_assertions(for_assert, 'smartphone', 'Поиск по слову Смартфон')


def test_add_to_wishlist(page=None):
    if not page:  # тест запускается отдельно
        page = PageSearchBuy(driver)
        page.authorization(driver)
    page.search.send_keys('Смартфон')  # тестирование поиска
    page.search_btn.click()
    page.wait_page_loaded()
    link_text = page.search_link.get_attribute('innerText')
    element = page.search_photo.find()
    action = ActionChains(driver)
    action.move_to_element(element).perform()  # наводим указатель на фото, чтобы появилась ссылка Добавить в Мои желания
    page.add_to_favorite.click()  # добавляем в Избранное
    page.favorite.click()  # переходим в Избранное
    link_text_fav = page.in_favorite.get_attribute('innerText')
    # проверяем, что в Избранное добавлен нужный товар
    search_buy_assertions(link_text, link_text_fav, 'Товар добавлен в Избранное')
    page.remove.click()   # удаляем товар, чтобы при повторном вызове теста не возникла ошибка


def test_add_to_shopcart(page=None):
    if not page:  # тест запускается отдельно
        page = PageSearchBuy(driver)
        page.authorization(driver)
        page.search.send_keys('Смартфон')
        page.search_btn.click()
        page.wait_page_loaded()
    buy_nums = int(page.buy_nums_before.get_attribute('innerText'))  # количество товаров в корзине до добавления товара
    page.search_link.click()
    page.wait_page_loaded()
    params_num = page.sku_property.find()
    # данный if определяет количество параметров товара. Если 1, то можно сразу переходить в Корзину
    # если больше, то сначала надо выбрать какой-нибудь параметр и потом переходить в Корзину.
    if len(params_num) == 1:
        driver.execute_script(
            "document.getElementsByClassName('next-btn next-large next-btn-primary addcart')[0].click();")
    else:
        driver.execute_script(
            "document.getElementsByClassName('sku-property-item')[0].className = 'sku-property-item selected';")
        driver.execute_script("document.getElementsByClassName('sku-property-item selected')[0].click();")
        driver.execute_script(
            "document.getElementsByClassName('next-btn next-large next-btn-primary addcart')[0].click();")
    page.go_basket.wait_to_be_clickable()
    page.go_basket.click()
    page.wait_page_loaded()
    buy_nums_new = int(page.buy_nums_after.get_attribute('innerText').split(' ')[1][1:-1])
    search_buy_assertions(buy_nums + 1, buy_nums_new, 'Количество покупок в Корзине увеличилось на 1')
    page.wait_page_loaded()
    # проверяем, изменилась ли сумма
    price_before = page.total_price.get_text()   # стоимость товаров в корзине до покупки
    page.buy_check.find()[2].click()   # отмечаем добавленный товар в Корзине
    time.sleep(3)
    price_after = page.total_price.get_attribute('innerText')
    search_buy_assertions(price_before, price_after, 'Сумма к оплате изменилась', 0)
    page.delete.click()   # удаляем товар, чтобы при повторном вызове теста не возникла ошибка
    page.ok_delete.wait_to_be_clickable()
    page.ok_delete.click()


# СЦЕНАРИЙ: 1. Авторизация; 2. Поиск; 3. Добавить в Избранное и удалить; 4. Добавить в Корзину и удалить
def test_search_addcart_favorite():
    page = PageSearchBuy(driver)
    page.authorization(driver)
    test_search(page)
    test_add_to_wishlist(page)
    page.go_back()
    page.go_back()
    test_add_to_shopcart(page)
