<template>
  <div>
    <h1>여기는 최상위 컴포넌트</h1>
    <!-- 3. 보여준다. -->
    <TodoList category="취업준비"></TodoList>
    <TodoList category="싸피"></TodoList>
    <TodoList category="guitar"></TodoList>
  </div>
</template>

<script>
// 1. 불러온다
import TodoList from './components/TodoList.vue'
// 2. 등록한다
export default {
  components: {
    TodoList,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
