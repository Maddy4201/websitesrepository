import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.account_login import Login
from utilities.read_properties import Read_Config_Data
from utilities.custom_logger import Log_Maker


class Test_Login_Account:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()
	invalid_username = Read_Config_Data.get_invalid_username()
	logger = Log_Maker.log_gen()

	def test_valid_login(self, setup):
		self.logger.info("**************Opened the browser****************")
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.user_login = Login(self.driver)
		self.user_login.enter_username(self.username)
		self.user_login.enter_password(self.password)
		self.user_login.click_login()
		self.logger.info("**************Logged into the account****************")
		page_title = self.driver.title
		print("Page title is: ", page_title)
		loginConfirmationText = self.user_login.visit_website_text()
		self.driver.close()
		self.logger.info("**********Login in test closed*********")
		# self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
		assert True

	def test_invalid_login(self, setup):
		self.logger.info("**********Launched browser for 2nd test case*********")
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.user_login = Login(self.driver)
		self.user_login.enter_username(self.invalid_username)
		self.user_login.enter_password(self.password)
		self.user_login.click_login()
		self.logger.info("**********Logged in*********")
		error_msg = self.user_login.get_error_msg()
		if error_msg == "These credentials do not match our records.":
			self.logger.info("**********Error message validated *********")
			assert True
		else:
			self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
			self.driver.close()
			assert False

	# self.driver.close()
	# self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
	# assert True
