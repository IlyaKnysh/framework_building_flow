from selenium import webdriver


class Driver:

    def __init__(self):
        self.driver = None

    def set_shared_driver(self, driver_):
        self.driver = driver_

    def get_shared_driver(self):
        return self.driver

    @staticmethod
    def create_browser():
        return webdriver.Chrome()


driver = Driver()
