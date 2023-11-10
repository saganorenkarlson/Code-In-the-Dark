<template>
    <div class="btn_overall" @click="onClick">{{ label }}</div>
    
  </template>
  
  <script>
import './Buttons.css'

  
export default {
  name: 'my-button',
  props: ['label'],
      methods: {
        onClick() {
          this.$emit('customClick');
        }
  }
}


  </script>

  <style>

.btn_overall{
    width: fit-content;
    height: 2.3rem;
    background-color: #282828;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #F1F1F1;
    font-size: 1.3em;
    font-weight: 100;
    margin: 10px 0px 10px 0px;
    padding: 0 2rem;

}

.btn_overall:hover{
    background-color: #181818;
    cursor: pointer;
}

</style>