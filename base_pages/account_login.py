from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
     username_field_id = "email"
     password_field_id = "password"
     login_button_xpath = "//button[@class='submit-button']"
     error_msg_xpath = "//span[@class='help-block']"
     visitWebsiteText_xpath = "//a[@id='visit-website_tooltip']"
     congratulations_popUp_xpath = "//button[normalize-space()='Check it later']"
     tooltip_popUp_xpath = "//button[@class='driver-popover-close-btn']"
     bogo_offer_popUp_xpath = "//button[contains(@class, 'close') and contains(@class, '__bogo_popup_close_event')]"

     def __init__(self, driver):
         self.driver = driver
         self.wait = WebDriverWait(driver, 10)

     def wait_for_loader_to_disappear(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.ID,"ajaxLoader")))
            print("Loader disappeared, proceeding...")
        except:
            print("No loader found or already disappeared.")

     def enter_username(self, username):
         self.wait.until(EC.visibility_of_element_located((By.ID, self.username_field_id))).send_keys(username)

     def enter_password(self, password):
         self.wait.until(EC.visibility_of_element_located((By.ID, self.password_field_id))).send_keys(password)

     def click_login (self):
         self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login_button_xpath ))).click()
         self.wait_for_loader_to_disappear()
         self.ignore_congratulations_popUp()
         self.ignore_tooltip_popUp()
         self.ignore_bogo_offer_popUp()

     def ignore_congratulations_popUp(self):
         try:
             congo_popUp = self.driver.find_element(By.XPATH, self.congratulations_popUp_xpath)
             if congo_popUp.is_displayed():
                 congo_popUp.click()
                 print("Pop-up appeared and was closed.")
         except TimeoutException:
            print("No pop-up appeared, continuing with the next step.")

         except NoSuchElementException:
             print("Pop-up not found, proceeding normally.")

     def ignore_tooltip_popUp(self):
         try:
             tooltip_popUp = self.driver.find_element(By.XPATH, self.tooltip_popUp_xpath)
             if tooltip_popUp.is_displayed():
                 tooltip_popUp.click()
                 print("Tooltip pop-up closed.")
         except (NoSuchElementException, TimeoutException):
             print("No Tooltip pop-up, moving on")

     def ignore_bogo_offer_popUp(self):
         try:
             bogo_popUp = self.driver.find_element(By.XPATH, self.bogo_offer_popUp_xpath)
             if bogo_popUp.is_displayed():
                 bogo_popUp.click()
                 print("BOGO Offer pop-up closed.")
         except (NoSuchElementException, TimeoutException):
             print("No Tooltip pop-up, moving on")

     def get_error_msg(self):
         return self.driver.find_element(By.XPATH, self.error_msg_xpath).text

     def visit_website_text(self):
         return self.driver.find_element(By.XPATH, self.visitWebsiteText_xpath).text
