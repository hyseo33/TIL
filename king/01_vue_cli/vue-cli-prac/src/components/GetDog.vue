<template>
  <div>
    <button v-on:click="getDogImage">멍멍!</button>
    <img v-bind:src="image">
  </div>
</template>

<script> 
  export default {
    
  }
</script>

<style>

</style>