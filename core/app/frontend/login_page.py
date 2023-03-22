from core.find_element import find_element


def get_submit_button():
    return find_element(value='login-button')


def get_username_field():
    return find_element(value='user-name')


def get_password_field():
    return find_element(value='password')