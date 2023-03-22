class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def item_price(self, item_name):
        return self.driver.find_element(by='xpath',
                                        value=f"//div[@class='inventory_item' and descendant::div[contains(text(), '{item_name}')]]//div[@class='inventory_item_price']")

    def item(self, item_name):
        return self.driver.find_element(by='xpath', value=f"//div[contains(text(), '{item_name}')]")
