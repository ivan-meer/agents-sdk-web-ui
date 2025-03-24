#!/bin/bash

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Функция вывода справки
show_help() {
    echo -e "${BLUE}Git Helper Script${NC}"
    echo "Использование: ./git-helper.sh [команда] [параметры]"
    echo ""
    echo "Команды:"
    echo "  new-feature   - Создать новую feature-ветку"
    echo "  new-bugfix    - Создать новую ветку для исправления бага"
    echo "  commit        - Создать коммит с проверками"
    echo "  merge         - Слить ветки с проверками"
    echo "  release       - Создать новый релиз"
    echo "  status        - Расширенный статус репозитория"
    echo "  sync          - Синхронизировать ветки"
    echo "  cleanup       - Очистить старые локальные ветки"
    echo ""
    echo "Примеры:"
    echo "  ./git-helper.sh new-feature agents-ui"
    echo "  ./git-helper.sh commit \"Добавить новый компонент agents\""
}

# Проверка наличия git
check_git() {
    if ! command -v git &> /dev/null; then
        echo -e "${RED}Git не установлен!${NC}"
        exit 1
    fi
}

# Создание feature-ветки
new_feature() {
    check_git
    if [ -z "$1" ]; then
        echo -e "${RED}Укажите название feature-ветки!${NC}"
        exit 1
    fi

    BRANCH_NAME="feature/$1"
    
    git checkout develop
    git pull origin develop
    git checkout -b "$BRANCH_NAME"
    
    echo -e "${GREEN}Создана новая feature-ветка: $BRANCH_NAME${NC}"
}

# Создание ветки для исправления бага
new_bugfix() {
    check_git
    if [ -z "$1" ]; then
        echo -e "${RED}Укажите название bugfix-ветки!${NC}"
        exit 1
    fi

    BRANCH_NAME="bugfix/$1"
    
    git checkout develop
    git pull origin develop
    git checkout -b "$BRANCH_NAME"
    
    echo -e "${GREEN}Создана новая bugfix-ветка: $BRANCH_NAME${NC}"
}

# Создание коммита с проверками
commit_changes() {
    check_git
    
    if [ -z "$1" ]; then
        echo -e "${RED}Укажите описание коммита!${NC}"
        exit 1
    fi

    # Проверка наличия незакоммиченных изменений
    if [[ -z $(git status -s) ]]; then
        echo -e "${YELLOW}Нет изменений для коммита!${NC}"
        exit 1
    fi

    # Запуск линтеров и тестов
    echo -e "${BLUE}Запуск линтеров...${NC}"
    npm run lint
    
    echo -e "${BLUE}Запуск тестов...${NC}"
    npm test

    # Добавление всех изменений
    git add .
    
    # Коммит с подписью
    git commit -m "$1" -m "$(date '+%Y-%m-%d %H:%M:%S')"
    
    echo -e "${GREEN}Коммит успешно создан: $1${NC}"
}

# Слияние веток с проверками
merge_branches() {
    check_git
    
    if [ -z "$1" ] || [ -z "$2" ]; then
        echo -e "${RED}Укажите исходную и целевую ветки!${NC}"
        exit 1
    fi

    SOURCE_BRANCH="$1"
    TARGET_BRANCH="$2"

    # Проверка существования веток
    git rev-parse --verify "$SOURCE_BRANCH" &> /dev/null
    if [ $? -ne 0 ]; then
        echo -e "${RED}Исходная ветка $SOURCE_BRANCH не существует!${NC}"
        exit 1
    fi

    git rev-parse --verify "$TARGET_BRANCH" &> /dev/null
    if [ $? -ne 0 ]; then
        echo -e "${RED}Целевая ветка $TARGET_BRANCH не существует!${NC}"
        exit 1
    fi

    # Переключение на целевую ветку
    git checkout "$TARGET_BRANCH"
    git pull origin "$TARGET_BRANCH"

    # Слияние
    git merge --no-ff "$SOURCE_BRANCH" -m "Merge $SOURCE_BRANCH into $TARGET_BRANCH"

    echo -e "${GREEN}Ветки успешно объединены!${NC}"
}

# Создание нового релиза
create_release() {
    check_git
    
    if [ -z "$1" ]; then
        echo -e "${RED}Укажите номер версии!${NC}"
        exit 1
    fi

    VERSION="$1"

    # Переключение на develop
    git checkout develop

    # Создание release-ветки
    git checkout -b "release/$VERSION"

    # Обновление версии в package.json
    npm version "$VERSION"

    # Коммит версии
    git add package.json
    git commit -m "Bump version to $VERSION"

    echo -e "${GREEN}Создан релиз: $VERSION${NC}"
}

# Расширенный статус репозитория
repo_status() {
    check_git
    
    echo -e "${BLUE}Статус репозитория:${NC}"
    git status
    
    echo -e "\n${BLUE}Локальные ветки:${NC}"
    git branch

    echo -e "\n${BLUE}Удаленные репозитории:${NC}"
    git remote -v
}

# Синхронизация веток
sync_branches() {
    check_git
    
    git fetch --all
    git pull --all

    echo -e "${GREEN}Репозиторий синхронизирован${NC}"
}

# Очистка старых локальных веток
cleanup_branches() {
    check_git
    
    # Удаление merged веток
    git branch --merged | egrep -v "(^\*|master|develop)" | xargs git branch -d

    echo -e "${GREEN}Старые ветки очищены${NC}"
}

# Основная логика скрипта
case "$1" in 
    new-feature)
        new_feature "$2"
        ;;
    new-bugfix)
        new_bugfix "$2"
        ;;
    commit)
        commit_changes "$2"
        ;;
    merge)
        merge_branches "$2" "$3"
        ;;
    release)
        create_release "$2"
        ;;
    status)
        repo_status
        ;;
    sync)
        sync_branches
        ;;
    cleanup)
        cleanup_branches
        ;;
    *)
        show_help
        ;;
esac

exit 0
