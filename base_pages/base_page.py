from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
