@echo off

call .venv\Scripts\activate.bat

python -m pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

pause


rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser edge
rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome
