class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(value='user-name')

    def get_password_field(self):
        return self.driver.find_element(value='password')

    def get_submit_button(self):
        return self.driver.find_element(value='login-button')
