from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base_pages.account_login import Login
from utilities.read_properties import Read_Config_Data


class Add_New_Product(Login):
	store_option_xpath = "//span[normalize-space()='Store']"
	product_services_option_xpath = "//span[normalize-space()='Products/Services']"
	add_product_button_id = "addProducts"
	product_type_select_xpath = "//select[@id='changeOnclick']"
	product_condition_select_xpath = "//select[@id='condition']"
	product_name_tag = "name"
	price_field_id = "price"
	discount_type_select_id = "discountType"
	discount_field_id = "discount"
	inventory_field_id = "stock_count"
	category_field_id = "select2-category-container"
	category_results_dropdown_xpath = "//ul[@id='select2-category-results']//li"  #This is the list
	create_category_button_xpath = "//a[normalize-space()='Create Category']"
	category_name_id = "categoryName"
	save_category_button_name = "btnSaveCategory"
	description_field_id = "description"
	publish_product_button_id = "saveProduct2"
	ignore_product_tooltip_xpath = "//button[@class='driver-popover-close-btn']"


	def __init__(self, driver):
		super().__init__(driver)

	def click_store_option(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.store_option_xpath))).click()

	def ingore_tooltip(self):
		try:
			tool_tip = self.driver.find_element(By.XPATH, self.ignore_product_tooltip_xpath)
			if tool_tip.is_displayed():
				tool_tip.click()
				self.wait_for_loader_to_disappear()
		except:
			print("Tooltip not present or already handled")

	def click_product_service_option(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.product_services_option_xpath))).click()
		self.wait_for_loader_to_disappear()

	def click_add_product_button(self):
		self.wait.until(EC.visibility_of_element_located((By.ID, self.add_product_button_id))).click()
		self.wait_for_loader_to_disappear()

	def select_product_type(self):
		self.wait_for_loader_to_disappear()
		select_product = self.driver.find_element(By.XPATH, self.product_type_select_xpath)
		slct = Select(select_product)
		slct.select_by_value("product")
		try:
			self.driver.find_element(By.XPATH, self.product_condition_select_xpath)
			return True
		except:
			return False

	def select_product_condition(self):
		try:
			select_condition = self.driver.find_element(By.XPATH, self.product_condition_select_xpath)
			selct = Select(select_condition)
			selct.select_by_value("refurbished")
			return True
		except:
			return False

	def enter_product_name(self, new_product_name):
		self.wait.until(EC.visibility_of_element_located((By.NAME, self.product_name_tag))).send_keys(new_product_name)

	def enter_price_amount(self, price):
		price_field = self.wait.until(EC.visibility_of_element_located((By.ID, self.price_field_id)))
		price_field.clear()
		price_field.send_keys(price)

	def select_discount_type(self):
		discount_type= self.driver.find_element(By.ID, self.discount_type_select_id)
		slect = Select(discount_type)
		slect.select_by_value("2")

	def enter_discount_amount(self, discount):
		self.wait.until(EC.visibility_of_element_located((By.ID, self.discount_field_id))).send_keys(discount)

	def enter_inventory_count(self):
		self.wait.until(EC.visibility_of_element_located((By.ID, self.inventory_field_id))).send_keys("10")

	def click_category_field(self):
		cat_field = self.wait.until(EC.visibility_of_element_located((By.ID, self.category_field_id)))
		cat_field.click()
		li_elements = self.driver.find_elements(By.TAG_NAME, "li")
		cat_text = Read_Config_Data.get_product_category()
		if li_elements:
			found = False
			for li in li_elements:
				actual_text = li.text.strip()
				if actual_text == cat_text:
					li.click()
					found = True
					break
			if not found:
				print("Category not found in list. Adding new.")
				self.add_new_category(cat_text)
		else:
			print("Step ELSE is being execute whihc adds new category")
			self.add_new_category(cat_text)

	def select_from_existing_category(self):
		categories = self.driver.find_elements(By.XPATH,self.category_results_dropdown_xpath)
		for category in categories:
			if category.text == "Cat CAT":
				category.click()
			else:
				print("Unable to click on category")
			break

	def add_new_category(self, name_of_category):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.create_category_button_xpath))).click()
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.visibility_of_element_located((By.ID, self.category_name_id))).send_keys(name_of_category)
		self.wait.until(EC.visibility_of_element_located((By.NAME, self.save_category_button_name))).click()
		self.wait_for_loader_to_disappear()

	def enter_description_text(self):
		self.wait.until(EC.visibility_of_element_located((By.ID, self.description_field_id))).send_keys("This is description of this product")

	def click_publish_product_button(self):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.visibility_of_element_located((By.ID, self.publish_product_button_id))).click()
		self.wait_for_loader_to_disappear()


