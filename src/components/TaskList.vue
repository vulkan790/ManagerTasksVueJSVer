<script>
import TaskItem from './TaskItem.vue'

export default {
    name: 'TaskList',
    components: { TaskItem },
    props: {
        tasks: {
            type: Array,
            required: true
        }
    },
    emits: ['delete-task']
}
</script>

<template>
    <div class="task-list">
        <TaskItem
            v-for="task in tasks"
            :key="task.id"
            :text="task.text"
            :onDelete="() => $emit('delete-task', task.id)"/>
    </div>
</template>

<style scoped>
.task-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}
</style>