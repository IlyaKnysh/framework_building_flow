from core.driver import driver


def find_element(*args, **kwargs):
    return driver.get_shared_driver().find_element(*args, **kwargs)
