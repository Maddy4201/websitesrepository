from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base_pages.account_login import Login


class Add_New_Update(Login):
	updates_posts_option_xpath = "//span[normalize-space()='Updates/Posts']"
	add_update_posts_xpath = "//span[normalize-space()='Add Update/Post']"
	update_title_field_id = "title"
	description_field_xpath = "//div[@class='note-editable panel-body']"
	save_post_button_id = "savePost"
	manage_update_post_xpath = "//span[normalize-space()='Manage Update/Post']"
	added_updates_xpath = "//ul[@class='timeline']//li//h3"
	edit_button_id = "editBtn"
	# //ul[@class='timeline']//li//div[2]//a[2][@id='editBtn']

	def __init__(self, driver):
		super().__init__(driver)

	def click_updates_post_option(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.updates_posts_option_xpath))).click()

	def click_add_update_posts_option(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.add_update_posts_xpath))).click()
		self.wait_for_loader_to_disappear()

	def enter_text_into_title_field(self, title_text):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.visibility_of_element_located((By.ID, self.update_title_field_id))).send_keys(title_text)

	def enter_description_text(self, description_text):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.description_field_xpath))).send_keys(description_text)

	def click_save_post_button(self):
		self.wait.until(EC.visibility_of_element_located((By.ID, self.save_post_button_id))).click()

	def click_manage_update_post(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.manage_update_post_xpath))).click()

	def search_added_update(self):
		self.wait_for_loader_to_disappear()
		updates = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.added_updates_xpath)))
		for update in updates:
			if update.text == "Test Update":
				print("Update Verified")
			else:
				print("Update not verified yet..")
			break


