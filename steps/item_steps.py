import allure

from core.app.frontend import item_page


@allure.step('Get price of item on item page')
def get_price():
    return item_page.get_price().text
