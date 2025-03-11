@echo off
cd /d %~dp0
echo Running PyCharm Automation Tests...
pytest -s -v -m "sanity" --html .\reports\report_chrome_one.html
rem pytest -s -v -m "regression" --html .\reports\report_chrome.html
pause
