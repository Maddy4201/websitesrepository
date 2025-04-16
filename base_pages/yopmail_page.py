import re
import time
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config_Data
import random


class Yop_Mail_Page:

	email_input_field_xpath = "//input[@class='ycptinput']"
	enter_arrow_xpath = "//i[@class='material-icons-outlined f36']"
	entered_mail_header_xpath = "//div[@class='bname']"
	iframe_xpath = "//iframe[@id='ifinbox']"


	def __init__(self, driver):
		self.driver = driver

	def get_email_from_file(self):
		with open("test_data/generated_email.txt", "r") as file:
			emails = file.readlines()
		# Get the last email used during registration
		return emails[-1].strip() if emails else None

	def get_otp_from_yopmail(self):
		# otp_email = Read_Config_Data.user_emai_id()
		self.driver.get("https://yopmail.com/en")
		email = self.get_email_from_file()
		self.driver.find_element(By.XPATH, "//input[@class='ycptinput']").send_keys(email)
		self.driver.find_element(By.XPATH, "//i[@class='material-icons-outlined f36']").click()
		email_header = self.driver.find_element(By.XPATH, "//div[@class='bname']")
		print(email_header.text)
		self.driver.switch_to.frame("ifinbox")
		email_list = self.driver.find_elements(By.CLASS_NAME, "m")
		if email_list:
			email_list[0].click()

		self.driver.switch_to.default_content()
		self.driver.switch_to.frame("ifmail")

		email_body = self.driver.find_element(By.XPATH, "//main[@class='yscrollbar']").text
		otp_match = re.search(r"\b\d{4}\b", email_body)
		return otp_match.group() if otp_match else None
		# if otp_match:
		# 	otp = otp_match.group()
		# 	print("OTP Found: ", otp)
		# else:
		# 	print("OTP not found")
		# time.sleep(5)



