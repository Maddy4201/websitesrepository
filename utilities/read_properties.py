import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config_Data:
	@staticmethod
	def get_url ():
		url = config.get('config_data', 'website_url')
		return url

	@staticmethod
	def get_username():
		username = config.get('config_data', 'username')
		return username

	@staticmethod
	def get_password():
		password = config.get('config_data', 'password')
		return password

	@staticmethod
	def get_invalid_username():
		invalid_username = config.get('config_data', 'invalid_username')
		return invalid_username

	@staticmethod
	def get_city_input():
		return config.get('city_data', 'city_input')  # Fetch city input for search

	@staticmethod
	def get_selected_city():
		return config.get('city_data', 'selected_city')

	@staticmethod
	def get_product_name():
		return config.get('product_data', 'product_name')

	@staticmethod
	def get_product_price():
		return config.get('product_data', 'product_price')

	@staticmethod
	def get_discount_amount():
		return config.get('product_data', 'discount_amount')

	@staticmethod
	def get_product_category():
		return config.get('product_data', 'product_category')

