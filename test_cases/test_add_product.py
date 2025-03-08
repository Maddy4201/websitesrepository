import time

from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config_Data
from base_pages.add_product_page import Add_New_Product


class Test_Execute_Add_Product:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()
	logger = Log_Maker().log_gen()


	def test_add_new_product(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.prod_obj = Add_New_Product(self.driver)
		self.prod_obj.enter_username(self.username)
		self.prod_obj.enter_password(self.password)
		self.prod_obj.click_login()
		self.logger.info("************ Logged in to add a product ************")
		self.prod_obj.click_store_option()
		self.prod_obj.click_product_service_option()
		self.prod_obj.click_add_product_button()
		self.prod_obj.select_product_type()
		self.prod_obj.select_product_condition()
		self.prod_obj.enter_product_name("New Test Product")
		self.prod_obj.enter_price_amount("199")
		self.prod_obj.select_discount_type()
		self.prod_obj.enter_discount_amount("50")
		self.prod_obj.enter_inventory_count()
		self.prod_obj.add_new_category("Herbal Product")
		self.logger.info("************ Filling in the product details ************")
		# self.prod_obj.enter_description_text()
		self.prod_obj.click_publish_product_button()
		self.logger.info("************ Published the product ************")
		time.sleep(5)
