# Руководство по участию в проекте AI Agents Platform

## 🤝 Как внести вклад

Мы очень рады, что вы хотите помочь нашему проекту! Вот несколько способов участия:

### 1. Сообщения об ошибках 🐞
- Проверьте существующие issue перед созданием нового
- Используйте шаблоны issue для описания проблемы
- Предоставьте максимально подробную информацию

### 2. Предложения новых функций ✨
- Откройте issue с описанием предлагаемой функциональности
- Объясните причину и потенциальную пользу

### 3. Pull Request (PR)

#### Процесс создания PR:
1. Форкните репозиторий
2. Создайте feature-ветку:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Внесите изменения
4. Проведите локальное тестирование
5. Commit с понятным описанием:
   ```bash
   git commit -m "Добавить: краткое описание функции"
   ```
6. Push в свой форк:
   ```bash
   git push origin feature/amazing-feature
   ```
7. Создайте Pull Request

### Рекомендации по разработке

#### Backend (Python)
- Следуйте PEP 8
- Используйте type hints
- Покрывайте код тестами
- Документируйте функции и классы

#### Frontend (Next.js)
- Используйте TypeScript
- Применяйте ESLint и Prettier
- Следуйте принципам React

### Соглашения

- Названия веток: `feature/`, `bugfix/`, `docs/`
- Префиксы commit-сообщений: 
  - `Добавить:` - новая функция
  - `Исправить:` - баг-фикс
  - `Рефакторинг:` - технические улучшения
  - `Docs:` - обновление документации

## Локальная разработка

### Настройка окружения
```bash
# Клонирование
git clone https://github.com/your-org/ai-agents-platform.git
cd ai-agents-platform

# Установка зависимостей
python -m venv venv
source venv/bin/activate  # Для Unix
venv\Scripts\activate    # Для Windows

# Backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### Запуск тестов
```bash
# Backend
pytest tests/

# Frontend
npm run test
```

## Кодекс поведения

- Уважайте других участников
- Будьте конструктивны
- Цените разнообразие мнений

## Вопросы?

Свяжитесь с нами:
- Email: support@aiagentsplatform.com
- Telegram: @AIAgentsPlatform

**Спасибо за ваш вклад! 🎉**
