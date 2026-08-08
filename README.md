# Task Manager (Vue.js + FastAPI)

Простое приложение для управления задачами, созданное на Vue.js (Frontend) и FastAPI (Backend). Позволяет добавлять, просматривать и удалять задачи с интуитивно понятным интерфейсом.

## Особенности

- **Добавление новых задач с валидацией пустого ввода**
- **Удаление задач в один клик**
- **Счётчик задач**
- **Интуитивно понятный UI/UX**
- **Сихронизация с сервером через FastAPI**
- **Хранение данных на сервере**

## Быстрый старт

### Предварительные требования
- **Node.js (версия 16 или выше)**
- **npm или yarn**
- **Python (версия 3.8 или выше)**
- **pip (менеджер пакетов для установки библиотек python)**

### Установка и запуск

1) **Клонируйте репозиторий**

```sh
git clone https://github.com/vulkan790/ManagerTasksVueJSVer.git
cd ManagerTasksVueJSVer
```

2) **Настройка и запуск бекенда (FastAPI)**

1. **Перейдите в папку с файлом crud.py**

```sh
cd src
```

2. **Установите зависимости python**

```sh
pip install fastapi uvicorn
```

3. **Запустите сервер FastAPI**

```sh
python -m uvicorn crud:app --port 8000 --reload
```

Сервер будет доступен по адресу: http://localhost:8000

4. **Проверьте работу API**

Откройте в браузере: http://localhost:8000/docs
Вы увидите интерактивную документацию Swagger UI с описанием всех эндпоинтов.

3) **Настройка и запуск Фронтенда (Vue.js)**

1. **Установите зависимости**

```sh
npm install
```

2. **Запустите в режиме разработки**

```sh
npm run dev
```

4) **Откройте в браузере**

5) **Сборка для production**

```sh
npm run build
```

## Структура (папка src)

```
├── components/                   # Компоненты Vue
│   ├── AddTaskForm.vue
│   ├── TaskItem.vue
│   └── TaskList.vue
├── App.vue                       # Главный компонент
├── crud.py                       # Файл с API (бекенд)
└── main.js                       # Точка входа Vue
```

## Используемые технологии

- **Frontend:** Vue.js
- **Backend:** FastAPI
- **Базовая вёрстка:** HTML/CSS
- **Сборка:** Vite

## API Эндпоинты

| Метод	 |  Эндпоинт	|           Описание          |
|--------|--------------|-----------------------------|
| GET	 | /tasks	    | Получить список всех задач  |
| POST	 | /tasks	    | Создать новую задачу        |
| GET	 | /tasks/{id}	| Получить задачу по ID       |
| DELETE | /tasks/{id}	| Удалить задачу по ID        |
| DELETE | /tasks	    | Удалить все задачи          |

# Task Manager (Vue.js)

A simple task management application built with Vue.js (Frontend) and FastAPI (Backend). Allows you to add, view, and delete tasks with an intuitive interface.

## Features

- **Add new tasks with empty input validation**
- **Delete tasks with one click**
- **Task counter**
- **Intuitive UI/UX**
- **Synchronization with server via FastAPI**
- **Server-side data storage**

## Quick Start

### Prerequisites
- **Node.js (version 16 or higher)**
- **npm или yarn**
- **Python (version 3.8 or higher)**
- **pip (package manager for installing Python libraries)**

### Installation and Running

1) **Clone the repository**

```sh
git clone https://github.com/vulkan790/ManagerTasksVueJSVer.git
cd ManagerTasksVueJSVer
```

2) **Backend Setup and Run (FastAPI)**

1. **Navigate to the folder with crud.py**

```sh
cd src
```

2. **Install Python dependencies**

```sh
pip install fastapi uvicorn
```

3. **Start the FastAPI server**

```sh
python -m uvicorn crud:app --port 8000 --reload
```

The server will be available at: http://localhost:8000

4. **Check API functionality**

Open in browser: http://localhost:8000/docs
You will see interactive Swagger UI documentation with all endpoint descriptions.

3) **Frontend Setup and Run (Vue.js)**

1. **Install dependencies**

```sh
npm install
```

2. **Run in development mode**

```sh
npm run dev
```

4) **Open in your browser**

5) **Build for production**

```sh
npm run build
```

## Structure (src folder)

```
├── components/                   # Vue Components
│   ├── AddTaskForm.vue
│   ├── TaskItem.vue
│   └── TaskList.vue
├── App.vue                       # Main Component
├── crud.py                       # API file (backend)
└── main.js                       # Vue entry point
```

## Technologies Used

- **Frontend:** Vue.js
- **Backend:** FastAPI
- **Basic layout:** HTML/CSS
- **Build tool:** Vite

## API Endpoints

| Method |  Endpoint	|        Description          |
|--------|--------------|-----------------------------|
| GET	 | /tasks	    | Get all tasks               |
| POST	 | /tasks	    | Create a new task           |
| GET	 | /tasks/{id}	| Get a task by ID            |
| DELETE | /tasks/{id}	| Delete a task by ID         |
| DELETE | /tasks	    | Delete all tasks            |