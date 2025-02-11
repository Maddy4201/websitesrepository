import time

from selenium import webdriver
from base_pages.account_login import Login
from base_pages.changeBusinessLocation import Change_Location
from utilities.read_properties import Read_Config_Data

class Test_City_Change:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()

	def test_new_city(self,setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.city_obj = Change_Location(self.driver)
		self.city_obj.enter_username(self.username)
		self.city_obj.enter_password(self.password)
		self.city_obj.click_login()
		time.sleep(4)
		self.city_obj.change_business_city()


