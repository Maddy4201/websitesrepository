import pytest
from selenium import webdriver
from base_pages.account_login import Login


class Test_Login_Account:

	website_url = "https://aspx.co.in/login"
	username = "testuser12@yopmail.com"
	password = "Testuser@1234"
	invalid_username = "hidufhei@eoidw.com"

	def test_valid_login(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.user_login = Login(self.driver)
		self.user_login.enter_username(self.username)
		self.user_login.enter_password(self.password)
		self.user_login.click_login()
		self.driver.close()
		assert True


	def test_invalid_login(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.user_login = Login(self.driver)
		self.user_login.enter_username(self.invalid_username)
		self.user_login.enter_password(self.password)
		self.user_login.click_login()
		error_msg = self.user_login.get_error_msg()
		print("Error msg: ",error_msg )
		self.driver.close()
		assert True

