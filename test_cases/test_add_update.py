import time

import pytest

from base_pages.add_an_update import Add_New_Update
from utilities.read_properties import Read_Config_Data
from utilities.custom_logger import Log_Maker


class Test_Execute_Add_Update:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()
	logger = Log_Maker().log_gen()

	@pytest.mark.skip(reason="Skipping this method for now")
	def test_add_new_update(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.update_obj = Add_New_Update(self.driver)
		self.update_obj.enter_username(self.username)
		self.update_obj.enter_password(self.password)
		self.update_obj.click_login()
		self.logger.info("********* Logged in for adding an update ***********")
		self.update_obj.click_updates_post_option()
		self.update_obj.click_add_update_posts_option()
		self.update_obj.enter_text_into_title_field("This is test title")
		self.update_obj.enter_description_text("Test Description Text")
		self.update_obj.click_save_post_button()
		self.logger.info("********* Added and saved an Update ***********")


	def test_edit_existing_update(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.update_obj = Add_New_Update(self.driver)
		self.update_obj.enter_username(self.username)
		self.update_obj.enter_password(self.password)
		self.update_obj.click_login()
		self.update_obj.click_updates_post_option()
		self.update_obj.click_manage_update_post()
		self.update_obj.search_added_update()
		time.sleep(5)

