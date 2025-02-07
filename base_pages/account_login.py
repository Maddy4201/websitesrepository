from selenium.webdriver.common.by import By


class Login:
     username_field_id = "email"
     password_field_id = "password"
     login_button_xpath = "//button[@class='submit-button']"
     error_msg_xpath = "//span[@class='help-block']"

     def __init__(self, driver):
         self.driver = driver

     def enter_username(self, username):
         self.driver.find_element(By.ID, self.username_field_id).send_keys(username)

     def enter_password(self, password):
         self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

     def click_login (self):
         self.driver.find_element(By.XPATH, self.login_button_xpath).click()

     def get_error_msg(self):
         return self.driver.find_element(By.XPATH, self.error_msg_xpath).text




