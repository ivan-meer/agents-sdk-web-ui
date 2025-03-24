@echo off
chcp 65001 > nul
cd /d %~dp0
start start_backend.bat
start start_frontend.bat
pause
