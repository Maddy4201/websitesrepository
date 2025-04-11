import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.account_login import Login
from base_pages.base_page import BasePage


class Register_An_Account(Login):
	signup_button_xpath = "//a[normalize-space()='Free Signup']"
	name_field_id = "name"
	email_field_id = "email"
	phone_no_field_id = "phone"
	password_field_id = "password"
	sign_up_button_id = "register"
	country_code_field_xpath = "//span[@id='select2-phonecode-container']"
	country_list_box_xpath = "//ul[@class='select2-results__options']//li"

	def __init__(self, driver):
		super().__init__(driver)

	def click_sign_up_button(self):
		self.driver.find_element(By.XPATH, self.signup_button_xpath).click()

	def switch_to_first_signup_window(self):
		main_window = self.driver.current_window_handle
		time.sleep(2)
		for handle in self.driver.window_handles:
			if handle != main_window:
				self.driver.switch_to.window(handle)
				break

	def enter_full_name(self, full_name):
		self.driver.find_element(By.ID, self.name_field_id).send_keys(full_name)

	def enter_email_address(self, email_address):
		self.driver.find_element(By.ID, self.email_field_id).send_keys(email_address)

	def select_country_code(self, code_text):
		self.driver.find_element(By.XPATH, self.country_code_field_xpath).click()
		counties_box = self.driver.find_elements(By.XPATH, self.country_list_box_xpath)
		for country in counties_box:
			# print(country.text)
			if code_text in country.text:
				country.click()
				break

	def enter_phone_no(self, phone_no):
		self.driver.find_element(By.ID, self.phone_no_field_id).send_keys(phone_no)

	def enter_new_password(self, password):
		self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

	def confirm_sign_up_button(self):
		self.driver.find_element(By.ID, self.sign_up_button_id).click()
		self.wait_for_loader_to_disappear()


