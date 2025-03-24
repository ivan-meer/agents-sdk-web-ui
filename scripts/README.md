# Служебные скрипты проекта

## Git Helper Script

### Обзор
`git-helper.sh` - мощный bash-скрипт для автоматизации Git-операций.

### Установка
```bash
chmod +x git-helper.sh
```

### Команды

| Команда      | Описание                                | Пример                                      |
|--------------|-------------------------------------------|---------------------------------------------|
| new-feature  | Создать feature-ветку                    | `./git-helper.sh new-feature agents-ui`     |
| new-bugfix   | Создать ветку для исправления бага        | `./git-helper.sh new-bugfix login-issue`    |
| commit       | Создать коммит с проверками              | `./git-helper.sh commit "Добавить компонент"`|
| merge        | Слить ветки с проверками                 | `./git-helper.sh merge feature develop`     |
| release      | Создать новый релиз                      | `./git-helper.sh release 1.0.0`             |
| status       | Расширенный статус репозитория            | `./git-helper.sh status`                    |
| sync         | Синхронизировать ветки                   | `./git-helper.sh sync`                      |
| cleanup      | Очистить старые локальные ветки          | `./git-helper.sh cleanup`                   |

### Требования
- Bash
- Git
- Node.js (для линтинга и тестов)
