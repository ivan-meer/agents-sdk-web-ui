@echo off
chcp 65001 > nul
call venv\Scripts\activate.bat
venv\Scripts\python.exe backend\main.py
pause
