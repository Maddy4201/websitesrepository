import time

import pytest

from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config_Data
from base_pages.get_business_card import Business_Card


class Test_Business_Card:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()
	logger = Log_Maker.log_gen()

	@pytest.mark.order(4)
	def test_download_busiCard(self, setup):
		self.logger.info("************ Running Test no. 04 *************")
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.card_obj = Business_Card(self.driver)
		self.card_obj.enter_username(self.username)
		self.card_obj.enter_password(self.password)
		self.card_obj.click_login()
		self.logger.info("************ Logged in successfully to dowload Business Card *************")
		self.card_obj.click_business_card_option()
		self.card_obj.get_card_page_text()
		self.card_obj.click_download_business_card()
		self.logger.info("************ Downloaded first business card *************")
		time.sleep(3)
		self.card_obj.click_next_card_arrow()
		# clicking download for next card
		self.card_obj.click_download_business_card()
		self.logger.info("************ Downloaded second business card *************")
		time.sleep(3)

