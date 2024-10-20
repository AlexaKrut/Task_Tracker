# Task Tracker CLI

Простое решение на Python [task-tracker](https://roadmap.sh/projects/task-tracker) для задания с проекта [roadmap.sh](https://roadmap.sh/).

## Описание проекта
Task Tracker CLI - это проект, который позволяет отслеживать и управлять задачами. Этот проект представляет собой простой командный интерфейс (CLI), который позволяет добавлять, обновлять и удалять задачи, а также отмечать их как выполненные или находящиеся в процессе выполнения.

## Установка

### Системные требования
- Python 3.x
- Кодовый редактор или IDE (например, VSCode, PyCharm)
- Git (для управления версиями проекта)

### Шаги установки
1. Клонируйте репозиторий проекта: 
   ```bash
   git clone git@github.com:AlexaKrut/Task_Tracker.git  
2. Перейдите в папку проекта
   ```bash
   cd Task_Tracker
3. Посмотрите справку о программе
   ```bash
   python3 task-cli.py -h
4. Запустите праграмму с необходимыми параметрами
   ```bash
   python3 task-cli.py <параметры>

## Использование

### Команды
- task-cli.py add "Задача" - добавить новую задачу
- task-cli.py update <id> "Задача" - обновить задачу с указанным идентификатором
- task-cli.py delete <id> - удалить задачу с указанным идентификатором
- task-cli.py mark-in-progress <id> - отметить задачу как находящуюся в процессе выполнения
- task-cli.py mark-done <id> - отметить задачу как выполненную
- task-cli.py list - список всех задач
- task-cli.py list done - список выполненных задач
- task-cli.py list todo - список невыполненных задач
- ttask-cli.py list in-progress - список задач, находящихся в процессе выполнения

### Примеры
   ```bash
  #Добавление новой задачи
  ttask-cli.py add "Купить продукты"

  #Обновление задачи по ее номеру
  task-cli.py update 1 "Купить продукты и приготовить ужин"

  #Удаление задачи по ее номер
  task-cli.py delete 1

  #Отметить задачу как начатую или сделанную
  task-cli.py mark-in-progress 1
  task-cli.py mark-done 1

  #Вывести все задачи
  task-cli.py list

  #Вывести задачи по сатусу
  task-cli.py list done
  task-cli.py list todo
  task-cli.py list in-progress
