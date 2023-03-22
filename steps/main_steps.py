import allure

from core.app.frontend import main_page


@allure.step('Get item price on the main page')
def get_item_price(item_name):
    return main_page.item_price(item_name).text


@allure.step('Open item page')
def open_item(item_name):
    return main_page.get_item(item_name).click()
