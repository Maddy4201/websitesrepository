from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.account_login import Login
from base_pages.base_page import BasePage


class Enter_The_OTP(Login):

	otp_field_xpath = "//input[@class='codeBox']"

	def __init__(self, driver):
		super().__init__(driver)

	def enter_otp(self, otp):
		otp_inputs = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.otp_field_xpath )))
		for i in range(4):
			otp_inputs[i].send_keys(otp[i])
