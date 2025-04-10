import time

import pytest
from base_pages.account_login import Login
from base_pages.registration_page import Register_An_Account
from utilities.read_properties import Read_Config_Data

class Test_Registration:
	home_page_url = Read_Config_Data.get_home_page_url()
	full_name = Read_Config_Data.full_user_name()
	email_address = Read_Config_Data.user_emai_id()
	phone_no = Read_Config_Data.user_phone_no()
	new_password = Read_Config_Data.user_password()

	def test_registration(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.home_page_url)
		self.reg_obj = Register_An_Account(self.driver)
		self.reg_obj.click_sign_up_button()
		self.reg_obj.switch_to_first_signup_window()
		self.reg_obj.enter_full_name(self.full_name)
		self.reg_obj.enter_email_address(self.email_address)
		self.reg_obj.enter_phone_no(self.phone_no)
		self.reg_obj.enter_new_password(self.new_password)
		self.reg_obj.confirm_sign_up_button()
		time.sleep(5)

