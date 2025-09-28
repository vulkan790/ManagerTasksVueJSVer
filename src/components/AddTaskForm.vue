<script>
import { ref } from 'vue'

export default {
    name: 'AddTaskForm',
    emits: ['add-task'],
    setup(props, { emit }) {
        const newTask = ref('')

        const handleSubmit = (e) => {
            e.preventDefault()
            if (newTask.value.trim()) 
            {
                emit('add-task', { id: Date.now().toString(), text: newTask.value.trim() })
                newTask.value = ''
            }
        }

        return { newTask, handleSubmit }
    }
}
</script>

<template>
    <form @submit="handleSubmit" class="add-task-form">
        <input
            type="text"
            v-model="newTask"
            placeholder="Введите новую задачу"
            class="task-input"/>
        <button type="submit" class="add-btn">Добавить</button>
    </form>
</template>

<style scoped>
.add-task-form {
  display: flex;
  gap: 10px;
  margin-bottom: 25px;
  background: white;
  padding: 15px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
}

.task-input {
  flex: 1;
  padding: 10px 14px;
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.3s ease;
  outline: none;
}

.task-input:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
}

.task-input::placeholder {
  color: #a0aec0;
}

.add-btn {
  padding: 10px 20px; 
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 14px; 
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.add-btn:hover {
  transform: translateY(-1px);
  background: #5a6fd8;
}

.add-btn:active {
  transform: translateY(0);
}
</style>