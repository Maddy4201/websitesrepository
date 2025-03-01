import time

from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base_pages.account_login import Login


class Change_Location(Login):
	business_profile_optn_xpath = "//a[@id='business_profile_nav']"
	edit_button_xpath = "//a[normalize-space()='EDIT']"
	city_field_xpath = "//span[@id='select2-city_id-container']"
	city_textField_xpath = "//input[@type='search']"
	cities_list_xpath = "//span[@class='select2-results']//li"
	save_button_xpath = "//button[@id='btn-save-business-profile']"

	def __init__(self, driver):
		super().__init__(driver)

	def click_business_profile_tab (self):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.business_profile_optn_xpath))).click()

	def click_edit_button (self):
		self.wait_for_loader_to_disappear()
		edit_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.edit_button_xpath)))
		self.driver.execute_script("arguments[0].scrollIntoView();", edit_button)
		self.wait.until(EC.element_to_be_clickable((By.XPATH, self.edit_button_xpath))).click()

	def click_city_field (self):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.element_to_be_clickable((By.XPATH, self.city_field_xpath))).click()

	def input_city_initial (self, city_input):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.element_to_be_clickable((By.XPATH, self.city_textField_xpath))).send_keys(city_input+" ")

	def select_opted_city (self, selected_city):
		self.wait_for_loader_to_disappear()
		try:
			cities = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.cities_list_xpath)))
			for cty in cities:
				if selected_city in cty.text:
					cty.click()
		except StaleElementReferenceException:
			print("Element became stale, retrying...")

	def click_save_location_button (self):
		save_location_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.save_button_xpath)))
		self.driver.execute_script("arguments[0].scrollIntoView();", save_location_button)
		self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))).click()


