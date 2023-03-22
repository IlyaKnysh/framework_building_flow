from hamcrest import assert_that, equal_to
from selenium import webdriver

from core.app.frontend.item_page import ItemPage
from core.app.frontend.login_page import LoginPage
from core.app.frontend.main_page import MainPage
from core.config.app_config import BASE_URL, USER


def test_auth():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    item_name = 'Sauce Labs Backpack'

    login_page = LoginPage(driver)
    login_page.get_username_field().send_keys(USER.username)
    login_page.get_password_field().send_keys(USER.password)
    login_page.get_submit_button().click()

    main_page = MainPage(driver)
    main_page_price = main_page.item_price(item_name).text
    main_page.item(item_name).click()

    item_page = ItemPage(driver)
    item_page_price = item_page.get_price().text

    assert_that(main_page_price, equal_to(item_page_price))
