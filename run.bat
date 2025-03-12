@echo off
cd /d %~dp0
echo Running PyCharm Automation Tests...
pytest -s -v .\test_cases\test_execute_login.py
rem pytest -s -v .\test_cases\test_add_update.py
rem pytest -s -v .\test_cases\test_add_product.py
rem pytest -s -v .\test_cases\test_changeBusiness_city.py
rem pytest -s -v .\test_cases\test_execute_buySubscription.py
rem pytest -s -v .\test_cases\test_download_businessCard.py
rem pytest -s -v -m "sanity" --html .\reports\report_chrome_one.html
rem pytest -s -v -m "regression" --html .\reports\report_chrome.html
pause
