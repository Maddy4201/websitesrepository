import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config_Data:

	@staticmethod
	def get_home_page_url():
		home_url = config.get('registration_data', 'home_page_url')
		return home_url

	@staticmethod
	def full_user_name():
		full_name = config.get('registration_data', 'full_name')
		return full_name

	@staticmethod
	def user_emai_id():
		new_user_email = config.get('registration_data', 'email_address')
		return new_user_email

	@staticmethod
	def user_phone_no():
		new_phone_no = config.get('registration_data', 'phone_no')
		return new_phone_no

	@staticmethod
	def user_password():
		new_password = config.get('registration_data', 'new_password')
		return new_password

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



