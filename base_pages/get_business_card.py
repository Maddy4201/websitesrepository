from base_pages.account_login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Business_Card(Login):
	business_card_option_xpath = "//span[normalize-space()='Business Card']"
	digital_card_text_xpath = "//div[@id='carousel-default']//h1"
	download_card_button_xpath = "//span[contains(@class, 'btn') and contains(@class, 'btn-danger')]"
	arrow_icon_xpath = "//span[contains(@class,'glyphicon') and contains (@class,'glyphicon-chevron-right')]"

	def __init__(self, driver):
		super().__init__(driver)

	def click_business_card_option(self):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.business_card_option_xpath ))).click()

	def get_card_page_text(self):
		page_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.digital_card_text_xpath)))
		print(page_text.text)

	def click_download_business_card(self):
		self.wait_for_loader_to_disappear()
		self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_card_button_xpath))).click()

	def click_next_card_arrow(self):
		self.wait.until(EC.element_to_be_clickable((By.XPATH, self.arrow_icon_xpath))).click()
