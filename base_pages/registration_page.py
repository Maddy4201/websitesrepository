import time

from selenium.webdriver.common.by import By

from base_pages.account_login import Login


class Register_An_Account(Login):
	signup_button_xpath = "//a[normalize-space()='Free Signup']"
	name_field_id = "name"
	email_field_id = "email"
	phone_no_field_id = "phone"
	password_field_id = "password"
	sign_up_button_id = "register"


	def __int__(self, driver):
		super().__init__(driver)

	def click_sign_up_button(self):
		self.driver.find_element(By.XPATH, self.signup_button_xpath).click()

	def switch_to_current_window(self):
		main_window = self.driver.current_window_handle
		time.sleep(2)
		for handle in self.driver.window_handles:
			if handle != main_window:
				self.driver.switch_to.window(handle)
				break

	def enter_full_name(self):
		self.driver.find_element(By.ID, self.name_field_id).send_keys("Test")

	def enter_email_address(self):
		self.driver.find_element(By.ID, self.email_field_id).send_keys("Test123@ymail.com")

	def enter_phone_no(self):
		self.driver.find_element(By.ID, self.phone_no_field_id).send_keys("9876123450")

	def enter_new_password(self):
		self.driver.find_element(By.ID, self.password_field_id).send_keys("Abcd@1234")

	def confirm_sign_up_button(self):
		self.driver.find_element(By.ID, self.sign_up_button_id)

