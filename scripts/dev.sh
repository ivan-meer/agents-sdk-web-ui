#!/bin/bash

# Запуск бэкенда и фронтенда в режиме разработки

# Проверка наличия .env файла
if [ ! -f .env ]; then
    echo "Файл .env не найден. Создаем из шаблона .env.example"
    cp .env.example .env
fi

# Запуск бэкенда
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Запуск фронтенда
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Функция для корректного завершения процессов
cleanup() {
    echo "Завершение процессов..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit 0
}

# Ловим сигналы завершения
trap cleanup SIGINT SIGTERM

# Ожидаем завершения
wait
