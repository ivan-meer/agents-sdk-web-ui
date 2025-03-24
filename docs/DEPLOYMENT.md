# Руководство по развертыванию AI Agents Platform

## 🌐 Варианты развертывания

### 1. Локальная разработка
- Docker Compose
- Минимальные требования к инфраструктуре

### 2. Staging/Production
- Kubernetes
- Облачные провайдеры (AWS, GCP, Azure)

## 🐳 Docker Compose

### Предварительная настройка
1. Установите Docker и Docker Compose
2. Склонируйте репозиторий
3. Создайте `.env`-файл

### Файл `.env`
```bash
# Backend
POSTGRES_USER=aiagent
POSTGRES_PASSWORD=secret
POSTGRES_DB=aiagents

# LLM Providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=...

# Security
SECRET_KEY=your_secret_key
```

### Команды
```bash
# Сборка и запуск
docker-compose up --build

# Остановка
docker-compose down

# Остановка с удалением томов
docker-compose down -v
```

## 🚀 Kubernetes (k8s)

### Манифесты
- `k8s/backend-deployment.yaml`
- `k8s/frontend-deployment.yaml`
- `k8s/postgres-deployment.yaml`

### Установка
```bash
kubectl apply -f k8s/
```

## 🔐 Безопасность

### SSL/TLS
- Используйте Let's Encrypt
- Настройте HTTPS
- Принудительное перенаправление на HTTPS

### Аутентификация
- OAuth 2.0
- JWT-токены
- Двухфакторная аутентификация

## 📊 Мониторинг

### Инструменты
- Prometheus
- Grafana
- ELK Stack (опционально)

### Метрики
- Использование ресурсов
- Производительность агентов
- Ошибки и исключения

## 🔄 CI/CD

### GitHub Actions
- Автоматическое тестирование
- Сборка Docker-образов
- Деплой в staging/production

### Workflow
1. Тестирование кода
2. Статический анализ
3. Сборка образов
4. Деплой

## 🌍 Масштабирование

### Горизонтальное масштабирование
- Stateless backend
- Кэширование Redis
- Балансировка нагрузки

### Стратегии
- Auto-scaling в Kubernetes
- Репликация backend-сервисов
- Кэширование запросов

## 💾 Резервное копирование

### База данных
- Регулярные дампы PostgreSQL
- Point-in-time recovery
- Репликация

### Конфигурации
- Храните в Git
- Используйте sealed secrets

## 🚨 Аварийное восстановление

### План действий
1. Резервное копирование данных
2. Репликация критически важных сервисов
3. Быстрое восстановление из резервных копий

## 📝 Чек-лист развертывания

- [ ] Настройка `.env`
- [ ] Проверка SSL/TLS
- [ ] Настройка мониторинга
- [ ] Тестирование резервного копирования
- [ ] Проверка масштабируемости

## 🆘 Поддержка

При возникновении проблем:
- Email: `devops@aiagentsplatform.com`
- Telegram: `@AIAgentsPlatformSupport`
