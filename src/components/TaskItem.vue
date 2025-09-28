<script>
export default {
    name: 'TaskItem',
    props: {
        text: {
            type: String,
            required: true
        },
        onDelete: {
            type: Function, 
            required: true
        }
    }
}
</script>

<template>
    <div class="task-item">
        <span>{{ text }}</span>
        <button @click="onDelete" class="delete-btn">Удалить</button>
    </div>
</template>

<style scoped>
.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  padding: 12px 16px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  animation: slideIn 0.3s ease-out;
}

.task-item:hover {
  transform: translateX(3px);
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.1);
}

.task-item span {
  font-size: 14px; 
  color: #2d3748;
  font-weight: 500;
  flex: 1;
  text-align: left;
  margin-right: 10px; 
}

.delete-btn {
  padding: 6px 12px;
  background: #f56565;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap; 
}

.delete-btn:hover {
  background: #e53e3e;
  transform: translateY(-1px);
}

.delete-btn:active {
  transform: translateY(0);
}
</style>