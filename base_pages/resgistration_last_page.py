from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_pages.account_login import Login


class Enter_Website_Details(Login):

	website_title_name = "business_name"
	business_category_select_id = "category"
	select_city_field_xpath = "//span[@title='Select City']"
	enter_city_field_xpath = "//input[@class='select2-search__field']"
	cities_list_xpath = "//ul[@role='tree']//li"
	postal_address_field_xpath = "//textarea[@id='address_1']"
	postal_code_field_xpath = "//input[@id='pincode']"
	show_address_checkbox_xpath = "//input[@name='show_address']"
	create_website_button_xpath = "//button[@type='submit']"
	congratulations_msg_xpath = "//h3[normalize-space()='Congratulations!']"

	def __init__(self, driver):
		super().__init__(driver)

	def enter_website_title(self, website_title):
		self.wait_for_loader_to_disappear()
		self.driver.find_element(By.NAME, self.website_title_name).send_keys(website_title)
		self.wait_for_loader_to_disappear()

	def select_website_category(self):
		self.wait_for_loader_to_disappear()
		busi_cat_dropdwn = Select(self.driver.find_element(By.ID, self.business_category_select_id))
		busi_cat_dropdwn.select_by_value("ART")

	def select_the_city(self, city_initial, city_name):
		self.driver.find_element(By.XPATH, self.select_city_field_xpath).click()
		self.driver.find_element(By.XPATH, self.enter_city_field_xpath).send_keys(city_initial)
		self.wait_for_loader_to_disappear()
		cities = self.driver.find_elements(By.XPATH, self.cities_list_xpath)
		for city in cities:
			if city_name in city.text:
				city.click()
				break

	def enter_postal_address(self):
		postal_address_field = self.driver.find_element(By.XPATH, self.postal_address_field_xpath)
		postal_address_field.clear()
		postal_address_field.send_keys("The next street, 1st lane, Mumbai")

	def enter_postal_code(self, postal_code):
		postal_code_field = self.driver.find_element(By.XPATH, self.postal_code_field_xpath)
		postal_code_field.clear()
		postal_code_field.send_keys(postal_code)

	def check_box_status_check(self):
		check_box = self.driver.find_element(By.XPATH, self.check_box_status_check)
		return check_box.is_selected()

	def click_create_website_button(self):
		self.driver.find_element(By.XPATH, self.create_website_button_xpath).click()

	def validate_website_creation_message(self):
		congo_msg = self.driver.find_element(By.XPATH, self.congratulations_msg_xpath)
		if congo_msg.is_displayed:
			print("New User Account has been created")
		else:
			print("Account was not created yet..")




