from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base_pages.account_login import Login


class Purchase_Subscription(Login):
	buy_subscription_button_xpath = "//span[normalize-space()='Buy Subscription']"
	yearly_plan_xpath = "//span[@class='pp-plan yearly active']"
	buy_subscription_second_button_xpath = "//a[@id='openPopup']"
	one_year_plan_xpath = "//div[@id='currentPlanDuration']"
	buy_button_xpath = "//button[@id='upgradeBtn']"
	pay_now_button_id = "show-payment-pop-up"
	grand_total_price_id = "formatted-grand-total"

	def __init__(self, driver):
		super().__init__(driver)

	def click_subscription_button(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.buy_subscription_button_xpath))).click()
		self.wait_for_loader_to_disappear()

	def select_yearly_plan(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.yearly_plan_xpath))).click()

	def click_buy_subscription(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.buy_subscription_second_button_xpath))).click()

	def select_one_year_plan(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.one_year_plan_xpath))).click()

	def click_buy_button(self):
		self.wait.until(EC.visibility_of_element_located((By.XPATH, self.buy_button_xpath))).click()
		self.wait_for_loader_to_disappear()

	def click_pay_now_button(self):
		self.wait.until(EC.visibility_of_element_located((By.ID, self.pay_now_button_id))).click()
		self.wait_for_loader_to_disappear()

	def get_grand_total_text(self):
		priceText = self.wait.until(EC.visibility_of_element_located((By.ID, self.grand_total_price_id)))
		print(priceText.text)





