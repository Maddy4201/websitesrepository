import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
	parser.addoption("--browser", action="store", default="chrome",
					 help="Specify the browser name: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
	return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
	global driver
	download_path = "C:\\Users\\Madhur\\PycharmProjects\\websitesproject\\downloaded_files"
	pereferences = {"download.default_directory": download_path,
					"download.prompt_for_download": False,
					"download.directory_upgrade": True,
					"safebrowsing.enabled": True
					}
	if browser == "chrome":
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_experimental_option("prefs", pereferences)
		driver = webdriver.Chrome(options=chrome_options)
	elif browser == "firefox":
		firefox_options = webdriver.FirefoxOptions()
		firefox_options.set_preference("browser.download.folderList", 2)
		firefox_options.set_preference("browser.download.dir", download_path)
		firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
		driver = webdriver.Firefox(options=firefox_options)
	elif browser == "edge":
		edge_options = webdriver.EdgeOptions()
		edge_options.add_experimental_option("prefs", pereferences)
		driver = webdriver.Edge(options=edge_options)
	else:
		raise ValueError("Unsupported browser")

	driver.maximize_window()
	yield driver
	driver.quit()

######## For pytest html reports #########
# hook for adding environment info into html report

def pytest_configure(config):
	config.stash[metadata_key]['Project name'] = 'Websites.co.in automation project'
	config.stash[metadata_key]['Test Module Name'] = 'Login / Sign Up'
	config.stash[metadata_key]['Tester Name'] = 'Madhur Soni'
	config.stash[metadata_key]['Month & Year'] = 'March 2025'

# hook to delete/modify environment info into html report
def pytest_metadata(metadata):
	metadata.pop('JAVA_HOME', None)
	metadata.pop('Plugins' , None)
