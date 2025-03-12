@echo off
cd /d %~dp0
echo Running PyCharm Automation Tests...

:: Optional: Clear old Allure reports
rmdir /s /q allure-results allure-report
mkdir allure-results
mkdir allure-report

:: Run only the tests you want, comment out (rem) others

rem pytest -s -v .\test_cases\test_execute_login.py --alluredir=allure-results
rem pytest -s -v .\test_cases\test_add_update.py --alluredir=allure-results
rem pytest -s -v .\test_cases\test_add_product.py --alluredir=allure-results
rem pytest -s -v .\test_cases\test_changeBusiness_city.py --alluredir=allure-results
rem pytest -s -v .\test_cases\test_execute_buySubscription.py --alluredir=allure-results
pytest -s -v .\test_cases\test_download_businessCard.py --alluredir=allure-results

:: Generate Allure report
allure generate allure-results -o allure-report --clean

:: Open Allure report in the browser (optional)
allure open allure-report

pause
