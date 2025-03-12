@echo off
cd /d %~dp0
echo Running PyCharm Automation Tests...

:: 🔴 Clear old Allure reports (Deletes old report data before running new tests)
rmdir /s /q %WORKSPACE%\allure-results %WORKSPACE%\allure-report
mkdir %WORKSPACE%\allure-results
mkdir %WORKSPACE%\allure-report

:: Check if a test file argument is provided
if "%1"=="" (
    echo No test file specified. Running all tests.
    pytest -s -v .\test_cases\ --alluredir=%WORKSPACE%\allure-results
) else (
    echo Running specified test: %1
    pytest -s -v .\test_cases\%1 --alluredir=%WORKSPACE%\allure-results
)

:: 🔵 Generate Allure report and clean old ones
allure generate %WORKSPACE%\allure-results -o %WORKSPACE%\allure-report --clean

:: 🔵 Open Allure report in the browser (optional)
allure open %WORKSPACE%\allure-report

pause
