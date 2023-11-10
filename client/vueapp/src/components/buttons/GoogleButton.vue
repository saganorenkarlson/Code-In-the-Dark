<template>
    <div class="google_btn" @click="onClick"> {{ label }}</div>
    
  </template>
  
  <script>

  
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

  <style>

.google_btn{
    width: 60%;
    height: 2.4rem;
    border: #282828 1px solid;
    background-color: #7d7d7d;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #F1F1F1;
    font-size: 0.7m;
    margin: 10px 0px 10px 0px;
 

}

.google_btn:hover{
    background-color: #5f5f5f;;
    cursor: pointer;
}

</style>