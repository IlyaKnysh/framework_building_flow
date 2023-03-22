import allure

from core.app.frontend import login_page


@allure.step('Authorize in the a system')
def authorize(user):
    login_page.get_username_field().send_keys(user.username)
    login_page.get_password_field().send_keys(user.password)
    login_page.get_submit_button().click()
