@echo off
chcp 65001 > nul
cd /d %~dp0
cd ..\..\frontend
pnpm dev
pause
