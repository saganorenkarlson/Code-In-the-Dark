<template>
    <div class="begin_btn" @click="onClick">{{ label }}</div>
    
  </template>
  
  <script>
import './Buttons.css'

  
export default {
  name: 'my-button',
  props: ['label'],
      methods: {
        onClick() {
          this.$emit('click');
        }
  }
}


  </script>