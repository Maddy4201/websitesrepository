from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_pages.account_login import Login


class Enter_Website_Details(Login):

	website_title_name = "business_name"
	business_category_select_id = "category"
	country_code_field_xpath = "//span[@id='select2-phonecode-container']"
	country_list_box_xpath = "//ul[@class='select2-results__options']//li"
	phone_no_field_xpath = "//input[@id='phone']"
	select_city_field_xpath = "//span[@id='select2-city-container']"
	enter_city_field_xpath = "//input[@class='select2-search__field']"
	cities_list_xpath = "//ul[@role='tree']//li"
	postal_address_field_xpath = "//textarea[@id='address_1']"
	postal_code_field_xpath = "//input[@id='pincode']"
	show_address_checkbox_xpath = "//input[@name='show_address']"
	create_website_button_xpath = "//button[@type='submit']"

	def __init__(self, driver):
		super().__init__(driver)

	def enter_website_title(self):
		self.driver.find_element(By.NAME, self.website_title_name).send_keys("Testofthebest")
		self.wait_for_loader_to_disappear()

	def select_website_categoty(self):
		self.wait_for_loader_to_disappear()
		busi_cat_dropdwn = Select(self.driver.find_element(By.ID, self.business_category_select_id))
		busi_cat_dropdwn.select_by_visible_text("ART")

	def select_country_code(self, code_text):
		self.driver.find_element(By.XPATH, self.phone_no_field_xpath).click()
		counties_box = self.driver.find_elements(By.XPATH, self.country_list_box_xpath)
		for country in counties_box:
			print(country.text)
			if code_text in country.text:
				country.click()
				break

	def enter_phone_number(self):
		self.driver.find_element(By.XPATH, self.phone_no_field_xpath).send_keys("78978979")

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





