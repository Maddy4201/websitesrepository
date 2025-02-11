from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
     username_field_id = "email"
     password_field_id = "password"
     login_button_xpath = "//button[@class='submit-button']"
     error_msg_xpath = "//span[@class='help-block']"
     visitWebsiteText_xpath = "//a[@id='visit-website_tooltip']"

     def __init__(self, driver):
         self.driver = driver
         self.wait = WebDriverWait(driver, 10)

     def enter_username(self, username):
         self.wait.until(EC.visibility_of_element_located((By.ID, self.username_field_id))).send_keys(username)

     def enter_password(self, password):
         self.wait.until(EC.visibility_of_element_located((By.ID, self.password_field_id))).send_keys(password)

     def click_login (self):
         self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login_button_xpath ))).click()

     def get_error_msg(self):
         return self.driver.find_element(By.XPATH, self.error_msg_xpath).text

     def visit_website_text(self):
         return self.driver.find_element(By.XPATH, self.visitWebsiteText_xpath).text




