<template>
    <div class="btn_finish" @click="onClick">{{ label }}</div>
    
  </template>
  
  <script>

  
export default {
  name: 'buttonFinish',
  props: ['label'],
      methods: {
        onClick() {
          this.$emit('click');
        }
  }
}


  </script>

  <style>

.btn_finish{
    width: 271px;
    height: 74px;
    left: 1091px;
    top: 12px;
    background: #363636;
    border-radius: 23px;
    font-size: 3.8rem;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #00897B;

}

.btn_finish:hover{
    background-color: #202020;
    cursor: pointer;
}

</style>