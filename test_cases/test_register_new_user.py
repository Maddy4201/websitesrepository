import time

import pytest
from base_pages.account_login import Login
from base_pages.registration_otp_page import Enter_The_OTP
from base_pages.registration_page import Register_An_Account
from base_pages.resgistration_last_page import Enter_Website_Details
from base_pages.yopmail_page import Yop_Mail_Page
from utilities.read_properties import Read_Config_Data

class Test_Registration:
	home_page_url = Read_Config_Data.get_home_page_url()
	full_name = Read_Config_Data.full_user_name()
	email_address = Read_Config_Data.user_emai_id()
	phone_no = Read_Config_Data.user_phone_no()
	new_password = Read_Config_Data.user_password()
	website_title = Read_Config_Data.new_website_title()
	country_code = Read_Config_Data.get_country_code()
	city_initials = Read_Config_Data.get_city_initials()
	city_name = Read_Config_Data.get_city_name()
	postal_code = Read_Config_Data.get_post_code()


	def test_registration(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.home_page_url)

		self.reg_obj = Register_An_Account(self.driver)
		self.reg_obj.click_sign_up_button()
		self.reg_obj.switch_to_first_signup_window()
		self.reg_obj.enter_full_name(self.full_name)
		self.reg_obj.enter_email_address(self.email_address)
		self.reg_obj.select_country_code(self.country_code)
		self.reg_obj.enter_phone_no(self.phone_no)
		self.reg_obj.enter_new_password(self.new_password)
		self.reg_obj.confirm_sign_up_button()

		original_tab = self.driver.current_window_handle

		# # # Open Yopmail in new tab
		self.driver.switch_to.new_window("tab")
		self.yop = Yop_Mail_Page(self.driver)
		self.otp = self.yop.get_otp_from_yopmail()
		print("Fetched OTP: ", self.otp)

		# Close Yopmail tab and switch back to original
		self.driver.close()
		self.driver.switch_to.window(original_tab)

		self.otp_page = Enter_The_OTP(self.driver)
		self.otp_page.enter_otp(self.otp)
		time.sleep(2)
		# self.otp_page.click_verify_button()

		self.last_page = Enter_Website_Details(self.driver)
		self.last_page.enter_website_title(self.website_title)
		self.last_page.select_website_category()
		self.last_page.select_the_city(self.city_initials, self.city_name)
		self.last_page.enter_postal_address()
		self.last_page.enter_postal_code(self.postal_code)
		self.last_page.click_create_website_button()
		time.sleep(5)

