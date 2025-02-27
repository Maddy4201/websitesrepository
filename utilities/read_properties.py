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
		return config.get('CITY', 'city_input')  # Fetch city input for search

	@staticmethod
	def get_selected_city():
		return config.get('CITY', 'selected_city')


