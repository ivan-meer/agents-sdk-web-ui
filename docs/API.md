# AI Agents Platform API Reference

## 🚪 Введение

Данный документ описывает REST и WebSocket API платформы управления ИИ-агентами.

## 🔐 Аутентификация

### JWT Token
- **Эндпоинт**: `/auth/token`
- **Метод**: POST
- **Параметры**:
  - `username`: Логин пользователя
  - `password`: Пароль

#### Пример запроса
```bash
curl -X POST https://api.aiagentsplatform.com/auth/token \
     -H "Content-Type: application/json" \
     -d '{"username": "user", "password": "password"}'
```

#### Ответ
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 3600
}
```

## 🤖 Агенты

### Получение списка агентов
- **Эндпоинт**: `/agents`
- **Метод**: GET
- **Параметры**:
  - `page`: Номер страницы (опционально)
  - `limit`: Количество агентов на странице (опционально)

#### Пример запроса
```bash
curl -X GET https://api.aiagentsplatform.com/agents \
     -H "Authorization: Bearer {access_token}"
```

#### Ответ
```json
{
    "agents": [
        {
            "id": "agent-001",
            "name": "Data Analyst Agent",
            "description": "Агент для анализа данных",
            "llm_provider": "OpenAI",
            "status": "active"
        },
        {
            "id": "agent-002",
            "name": "Customer Support Agent",
            "description": "Агент для поддержки клиентов",
            "llm_provider": "Anthropic",
            "status": "inactive"
        }
    ],
    "total": 2,
    "page": 1,
    "limit": 10
}
```

### Создание агента
- **Эндпоинт**: `/agents`
- **Метод**: POST
- **Параметры**:
  - `name`: Название агента
  - `description`: Описание
  - `llm_provider`: Провайдер LLM
  - `tools`: Список инструментов
  - `config`: Дополнительная конфигурация

#### Пример запроса
```bash
curl -X POST https://api.aiagentsplatform.com/agents \
     -H "Authorization: Bearer {access_token}" \
     -H "Content-Type: application/json" \
     -d '{
         "name": "Sales Insights Agent",
         "description": "Агент для анализа продаж",
         "llm_provider": "OpenAI",
         "tools": ["data_analysis", "reporting"],
         "config": {
             "model": "gpt-4",
             "temperature": 0.7
         }
     }'
```

## 🌐 WebSocket: Взаимодействие с Агентами

### Подключение
- **Endpoint**: `ws://api.aiagentsplatform.com/agents/{agent_id}/chat`

### Протокол обмена сообщениями
```json
{
    "type": "message",
    "agent_id": "agent-001",
    "content": "Проанализируй данные о продажах за последний квартал",
    "context": {}
}
```

## 🛠 Инструменты Агентов

### Получение списка доступных инструментов
- **Эндпоинт**: `/tools`
- **Метод**: GET

#### Пример ответа
```json
{
    "tools": [
        {
            "id": "data_analysis",
            "name": "Анализ данных",
            "description": "Инструмент для статистического анализа",
            "category": "analytics"
        },
        {
            "id": "web_search",
            "name": "Поиск в интернете",
            "description": "Инструмент для поиска информации",
            "category": "research"
        }
    ]
}
```

## 📊 Мониторинг Агентов

### Получение статистики агента
- **Эндпоинт**: `/agents/{agent_id}/stats`
- **Метод**: GET

#### Пример ответа
```json
{
    "agent_id": "agent-001",
    "total_interactions": 1024,
    "success_rate": 0.92,
    "average_response_time": 1.5,
    "last_interaction": "2024-03-24T12:00:00Z"
}
```

## 🚨 Коды ошибок

| Код | Описание |
|-----|----------|
| 200 | Успешный запрос |
| 400 | Некорректный запрос |
| 401 | Не авторизован |
| 403 | Доступ запрещен |
| 404 | Ресурс не найден |
| 500 | Внутренняя ошибка сервера |

## 🔒 Безопасность

- Все эндпоинты требуют JWT-токен
- HTTPS для всех запросов
- Ограничение количества запросов
- Шифрование чувствительных данных

## 📝 Версионность API

- Текущая версия: `v1`
- Base URL: `https://api.aiagentsplatform.com/v1`

## 🆘 Поддержка

При возникновении вопросов:
- Email: `support@aiagentsplatform.com`
- Telegram: `@AIAgentsPlatform`
