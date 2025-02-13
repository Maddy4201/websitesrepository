import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
	parser.addoption("--browser", action="store", default="chrome",
					 help="Specify the browser name: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
	return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
	global driver
	if browser == "chrome":
		driver = webdriver.Chrome()
	elif browser == "firefox":
		driver = webdriver.Firefox()
	elif browser == "edge":
		driver = webdriver.Edge()
	else:
		raise ValueError("Unsupported browser")

	return driver

######## For pytest html reports #########
# hook for adding environment info into html report

def pytest_configure(config):
	config.stash[metadata_key]['Project name'] = 'Websites.co.in automation project'
	config.stash[metadata_key]['Test Module Name'] = 'Login / Sign Up'
	config.stash[metadata_key]['Tester Name'] = 'Madhur Soni'
	config.stash[metadata_key]['Month & Year'] = 'Feb 2025'

# hook to delete/modify environment info into html report
def pytest_metadata(metadata):
	metadata.pop('JAVA_HOME', None)
	metadata.pop('Plugins' , None)
