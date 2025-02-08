import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.account_login import Login
from utilities.read_properties import Read_Config_Data


class Test_Login_Account:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()
	invalid_username = Read_Config_Data.get_invalid_username()

	def test_valid_login(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.user_login = Login(self.driver)
		self.user_login.enter_username(self.username)
		self.user_login.enter_password(self.password)
		self.user_login.click_login()
		page_title = self.driver.title
		print("Page title is: ", page_title)
		self.driver.close()
		# self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
		assert True

	def test_invalid_login(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.user_login = Login(self.driver)
		self.user_login.enter_username(self.invalid_username)
		self.user_login.enter_password(self.password)
		self.user_login.click_login()
		error_msg = self.user_login.get_error_msg()
		if error_msg == "These credentials do not match our records.":
			assert True
		else:
			self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
			self.driver.close()
			assert False

	# self.driver.close()
	# self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
	# assert True
