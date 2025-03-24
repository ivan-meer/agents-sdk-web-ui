@echo off
chcp 65001 > nul
cd /d %~dp0

echo Установка зависимостей backend...
cd ..\..\backend

echo Создание виртуального окружения...
python -m venv venv

echo Активация виртуального окружения...
call venv\Scripts\activate.bat  <-- АКТИВАЦИЯ СРАЗУ ПОСЛЕ СОЗДАНИЯ

echo Переустановка зависимостей backend (включая python-dotenv)...
pip install -r ..\requirements.txt  <-- ПЕРЕУСТАНОВКА ЗАВИСИМОСТЕЙ

echo Установка зависимостей frontend...
cd ..\..\frontend
cd frontend
pnpm install

echo Установка завершена!
cd ..\scripts\win
pause
