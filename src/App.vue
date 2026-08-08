<script>
import { ref, watch, onMounted } from 'vue'
import AddTaskForm from './components/AddTaskForm.vue'
import TaskList from './components/TaskList.vue'

export default {
  name: 'App',
  components: {
    AddTaskForm,
    TaskList
  },
  setup() {
    const tasks = ref([])

    const fetchTasks = async () => {
      try
      {
        const responce = await fetch("http://localhost:8000/tasks")
        if (!responce.ok)
          throw new Error("Ошибка загрузки")
        tasks.value = await responce.json()
      }
      catch (e)
      {
        console.error("Не удалось загрузить задачи: ", e)
        tasks.value = []
      }
    }

    const handleAddTask = async (taskText) => {
      try
      {
        const responce = await fetch("http://localhost:8000/tasks", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ text: taskText })
        })
        if (!responce.ok)
          throw new Error("Ошибка добавления")
        const newTask = await responce.json()
        tasks.value.push(newTask)
      }
      catch (e)
      {
        console.error("Не удалось добавить задачу: ", e)
        alert("Не удалось добавить задачу, попробуйте позже")
      }
    }

    const handleDeleteTask = async (taskId) => {
      try
      {
        const responce = await fetch(`http://localhost:8000/tasks/${taskId}`, {
          method: "DELETE"
        })
        if (!responce.ok)
          throw new Error("Ошибка удаления")
        tasks.value = tasks.value.filter(task => task.id !== taskId)
      }
      catch (e)
      {
        console.error("Не удалось удалить задачу: ", e)
        alert("Не удалось удалить задачу, попробуйте позже")
      }
    }

    onMounted(fetchTasks)

    return {
      tasks,
      handleAddTask,
      handleDeleteTask
    }
  }
}
</script>

<template>
  <div class="App">
    <h1>Менеджер задач</h1>
    <AddTaskForm @add-task="handleAddTask" />
    <TaskList 
      :tasks="tasks" 
      @delete-task="handleDeleteTask" />
    <div class="task-counter">
      Всего задач: {{ tasks.length }}
    </div>
  </div>
</template>

<style>
.App {
  text-align: center;
  justify-content: center;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  min-height: 100vh;
  max-width: 400px;
  width: 100%;
}

h1 {
  text-align: center;
  color: #000;
  font-size: 2rem;
  margin-bottom: 25px;
  font-weight: 300;
}

.task-counter {
  text-align: center;
  color: #2d3748;
  font-size: 14px;
  font-weight: 500;
  background: rgba(102, 126, 234, 0.05);
  padding: 12px;
  border-radius: 8px;
  border: 1px solid rgba(102, 126, 234, 0.1);
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>