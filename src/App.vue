<script>
import { ref } from 'vue'
import AddTaskForm from './components/AddTaskForm.vue'
import TaskList from './components/TaskList.vue'

export default {
  name: 'App',
  components: {
    AddTaskForm,
    TaskList
  },
  setup() {
    const tasks = ref([
      { id: '1', text: 'Почитать книгу' },
      { id: '2', text: 'Сходить в спортзал' }
    ])

    const handleAddTask = (newTask) => {
      tasks.value.push(newTask)
    }

    const handleDeleteTask = (taskId) => {
      tasks.value = tasks.value.filter(task => task.id !== taskId)
    }

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