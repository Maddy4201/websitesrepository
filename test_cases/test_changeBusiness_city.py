import time

from selenium import webdriver
from base_pages.account_login import Login
from base_pages.changeBusinessLocation import Change_Location
from utilities.read_properties import Read_Config_Data

class Test_City_Change:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()
	city_input = Read_Config_Data.get_city_input()
	selected_city = Read_Config_Data.get_selected_city()

	def test_new_city(self,setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.city_obj = Change_Location(self.driver)
		self.city_obj.enter_username(self.username)
		self.city_obj.enter_password(self.password)
		self.city_obj.click_login()
		self.city_obj.click_business_profile_tab()
		self.city_obj.click_edit_button()
		self.city_obj.click_city_field()
		self.city_obj.input_city_initial(self.city_input)
		self.city_obj.select_opted_city(self.selected_city)
		self.city_obj.click_save_location_button()





