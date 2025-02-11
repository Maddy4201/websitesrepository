from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.account_login import Login


class Change_Location(Login):
	business_profile_optn_xpath = "//a[@id='business_profile_nav']"
	edit_button_xpath = "//a[normalize-space()='EDIT']"
	city_field_xpath = "//span[@id='select2-city_id-container']"
	city_textField_xpath = "//input[@type='search']"
	city_results_xpath = "//ul[@id='select2-city_id-results']//li[4]"
	save_button_xpath = "//button[@id='btn-save-business-profile']"

	def __init__(self, driver):
		super().__init__(driver)

	def change_business_city(self):
		self.driver.implicitly_wait(10)
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.business_profile_optn_xpath))).click()
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.edit_button_xpath))).click()
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.city_field_xpath))).click()
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.city_textField_xpath))).send_keys("new ")
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.city_results_xpath))).click()
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.save_button_xpath))).click()

