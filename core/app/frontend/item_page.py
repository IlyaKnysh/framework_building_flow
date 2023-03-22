class ItemPage:

    def __init__(self, driver):
        self.driver = driver

    def get_price(self):
        return self.driver.find_element(by='xpath', value=f"//div[@class='inventory_details_price']")
