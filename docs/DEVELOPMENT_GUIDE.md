# 🚀 Руководство разработчика AI Agents SDK

## 📋 Оглавление

1. [Введение](#введение)
2. [Настройка окружения](#настройка-окружения)
3. [Структура проекта](#структура-проекта)
4. [Разработка Backend](#разработка-backend)
5. [Разработка Frontend](#разработка-frontend)
6. [Тестирование](#тестирование)
7. [Развертывание](#развертывание)
8. [Рекомендации](#рекомендации)

## 🌟 Введение

Данное руководство предназначено для разработчиков, желающих внести вклад в развитие AI Agents SDK или использовать его в своих проектах.

## 🛠 Настройка окружения

### Предварительные требования

- 🐍 Python 3.9+
- 📦 Node.js 18+
- 🐳 Docker (опционально)
- 🖥 ОС: Windows, macOS, Linux

### Шаги установки

```bash
# Клонирование репозитория
git clone https://github.com/ivan-meer/agents-sdk-web-ui.git
cd agents-sdk-web-ui

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows

# Установка зависимостей Backend
pip install -r backend/requirements.txt

# Установка зависимостей Frontend
cd frontend
npm install
```

## 📂 Структура проекта

```
agents-sdk-web-ui/
├── backend/             # Python Backend
│   ├── agent_platform/  # Ядро платформы агентов
│   ├── api/             # REST и WebSocket API
│   ├── models/          # Модели данных
│   └── tests/           # Юнит-тесты
│
├── frontend/            # Next.js Frontend
│   ├── src/
│   │   ├── components/  # React-компоненты
│   │   ├── app/         # Маршрутизация
│   │   └── styles/      # Стили
│   └── tests/           # Frontend тесты
│
├── docs/                # Документация
└── scripts/             # Служебные скрипты
```

## 🔧 Разработка Backend

### Соглашения по коду

- Использовать typing hints
- Следовать PEP8
- Документировать функции и классы
- Максимальная длина строки: 120 символов

### Создание нового агента

```python
from agent_platform.core import BaseAgent

class MyCustomAgent(BaseAgent):
    """Пример кастомного агента."""
    
    def __init__(self, config):
        super().__init__(config)
    
    async def process_task(self, task):
        """Обработка задачи агентом."""
        # Логика выполнения задачи
        pass
```

## 💻 Разработка Frontend

### Соглашения

- TypeScript с строгой типизацией
- Использовать React Hooks
- Компоненты с минимальной связанностью
- Styled-components или Tailwind CSS

### Пример компонента

```typescript
import React from 'react';

interface AgentProps {
  name: string;
  capabilities: string[];
}

const AgentComponent: React.FC<AgentProps> = ({ name, capabilities }) => {
  return (
    <div>
      <h2>{name}</h2>
      <ul>
        {capabilities.map(cap => <li key={cap}>{cap}</li>)}
      </ul>
    </div>
  );
};

export default AgentComponent;
```

## 🧪 Тестирование

### Backend тесты

```bash
# Запуск тестов
pytest backend/tests/

# Покрытие кода
pytest --cov=backend
```

### Frontend тесты

```bash
# Запуск тестов
npm test
```

## 🚢 Развертывание

### Локальный запуск

```bash
# Backend
python backend/main.py

# Frontend
npm run dev
```

### Docker

```bash
# Сборка и запуск
docker-compose up --build
```

## 🌈 Рекомендации

- Декомпозируйте сложную логику
- Минимизируйте побочные эффекты
- Используйте dependency injection
- Постоянно обновляйте зависимости
- Следите за безопасностью кода

## 🤝 Contributing

1. Форкните репозиторий
2. Создайте feature-ветку
3. Commits с понятными сообщениями
4. Создайте Pull Request
5. Пройдите Code Review

## 📚 Дополнительные ресурсы

- [Документация архитектуры](/docs/ARCHITECTURE.md)
- [Руководство по API](/docs/API.md)
- [Политика безопасности](/SECURITY.md)

**Успехов в разработке!** 🚀
