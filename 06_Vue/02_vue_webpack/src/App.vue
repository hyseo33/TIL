<template>
  <div>
    <h1>여기는 최상위 컴포넌트</h1>
    <TodoList category="취업준비"></TodoList>
    <TodoList category="싸피"></TodoList>
    <TodoList category="guitar"></TodoList>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'

export default {
  components: {
    TodoList,
  }
}
</script>

<style>

</style>