# Руководство по участию в проекте AI Agents Platform

## 🚀 Начало работы

### Предварительные требования

- **Python**: 3.9+
- **Node.js**: 18+
- **Менеджеры пакетов**: 
  - npm
  - yarn
  - pnpm (рекомендуется)
- **Git**: 2.x+

### Установка окружения

1. Клонирование репозитория
```bash
git clone https://github.com/your-org/ai-agents-platform.git
cd ai-agents-platform
```

2. Настройка Backend
```bash
# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Для Unix/macOS
venv\Scripts\activate     # Для Windows

# Установка зависимостей
pip install -r backend/requirements.txt
```

3. Настройка Frontend
```bash
cd frontend
npm install  # или yarn, или pnpm
```

## 🤝 Процесс разработки

### Ветвление

- `main`: Стабильная версия
- `develop`: Основная ветка разработки
- `feature/`: Новые функции
- `bugfix/`: Исправление ошибок
- `hotfix/`: Срочные исправления

### Создание feature-ветки

```bash
# Используйте скрипт
./scripts/git-helper.sh new-feature your-feature-name

# Или вручную
git checkout -b feature/your-feature-name develop
```

### Коммиты

- Используйте скрипт для коммитов:
```bash
./scripts/git-helper.sh commit "Краткое описание изменений"
```

### Правила коммитов

- `Добавить:` - новая функциональность
- `Исправить:` - баг-фикс
- `Рефакторинг:` - технический долг
- `Docs:` - обновление документации
- `Стиль:` - форматирование кода

## 🧪 Тестирование

### Backend (Python)
```bash
cd backend
pytest tests/
```

### Frontend (Next.js)
```bash
cd frontend
npm test
```

## 🔍 Линтинг

### Python
```bash
cd backend
pylint **/*.py
```

### TypeScript/React
```bash
cd frontend
npm run lint
```

## 📦 Сборка и деплой

### Локальная разработка
```bash
# Backend
cd backend
python main.py

# Frontend
cd frontend
npm run dev
```

### Docker
```bash
docker-compose up --build
```

## 🤔 Часто задаваемые вопросы

### Как начать разработку?
1. Форкните репозиторий
2. Клонируйте свой форк
3. Создайте feature-ветку
4. Внесите изменения
5. Создайте Pull Request в `develop`

### Что делать, если возникли проблемы с зависимостями?
- Используйте `./scripts/git-helper.sh` для управления зависимостями
- Очистите кэш npm: `npm cache clean --force`
- Попробуйте `npm install --legacy-peer-deps`

## 🛡️ Кодекс поведения

- Уважайте других участников
- Будьте конструктивны
- Следуйте принципам OpenSource

## 📞 Контакты

- **Email**: support@aiagentsplatform.com
- **Telegram**: [@AIAgentsPlatform](https://t.me/AIAgentsPlatform)
- **Discord**: [Присоединиться](https://discord.gg/your-invite)

## 📄 Лицензия

Проект распространяется под лицензией MIT. 
Подробности в файле [LICENSE](LICENSE).

**Спасибо за ваш вклад! 🎉**
