from selenium import webdriver
from base_pages.account_login import Login
from base_pages.buy_subscription import Purchase_Subscription
from utilities.read_properties import Read_Config_Data


class Test_Buy_Subscription:
	website_url = Read_Config_Data.get_url()
	username = Read_Config_Data.get_username()
	password = Read_Config_Data.get_password()


	def test_get_subscription(self, setup):
		self.driver = setup
		self.driver.maximize_window()
		self.driver.get(self.website_url)
		self.buySub_obj = Purchase_Subscription(self.driver)
		self.buySub_obj.enter_username(self.username)
		self.buySub_obj.enter_password(self.password)
		self.buySub_obj.click_login()
		self.buySub_obj.click_subscription_button()
		self.buySub_obj.select_yearly_plan()
		self.buySub_obj.click_buy_subscription()
		self.buySub_obj.select_one_year_plan()
		self.buySub_obj.click_buy_button()
		self.buySub_obj.click_pay_now_button()



