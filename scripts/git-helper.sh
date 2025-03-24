#!/bin/bash

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Базовая директория проекта
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Функция проверки и установки зависимостей
install_dependencies() {
    # Очистка кэша npm
    npm cache clean --force

    # Установка глобальных пакетов если нужно
    npm install -g npm@latest pnpm@latest yarn@latest jest@latest

    # Установка Python зависимостей
    if [ -f "$PROJECT_ROOT/backend/requirements.txt" ]; then
        echo -e "${BLUE}Установка Python зависимостей...${NC}"
        cd "$PROJECT_ROOT/backend"
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
    fi

    # Установка Frontend зависимостей
    if [ -f "$PROJECT_ROOT/frontend/package.json" ]; then
        echo -e "${BLUE}Установка Frontend зависимостей...${NC}"
        cd "$PROJECT_ROOT/frontend"
        
        # Последовательность попыток установки
        npm install --legacy-peer-deps || \
        npm install --force || \
        yarn install || \
        pnpm install || \
        npm install
    fi
}

# Остальные функции остаются прежними...

# Функция коммита с проверками
commit_changes() {
    # Установка зависимостей перед проверкой
    install_dependencies

    # Проверка Git-конфигурации
    check_git_config

    if [ -z "$1" ]; then
        echo -e "${RED}Укажите описание коммита!${NC}"
        exit 1
    fi

    # Возврат в корень проекта
    cd "$PROJECT_ROOT"

    # Проверка наличия незакоммиченных изменений
    if [[ -z $(git status -s) ]]; then
        echo -e "${YELLOW}Нет изменений для коммита!${NC}"
        exit 1
    fi

    # Добавление всех измененных файлов
    git add .
    
    # Коммит с подписью
    git commit -m "$1" -m "$(date '+%Y-%m-%d %H:%M:%S')"
    
    echo -e "${GREEN}Коммит успешно создан: $1${NC}"
}

# Основная логика и другие функции остаются прежними...

exit 0
