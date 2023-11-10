<template>
    <div class="card" > 

      <div class="left_div">
      <slot name="left"></slot>
    </div>

      <div class="right_div"> 
    <slot name="right"></slot>
    </div>
  </div>
  </template>
  
  <script>


  
export default {
  name: 'card-sign-up',
  props: ['label'],
      
}


  </script>


<style>
.card{
  background: rgb(150,150,150);
  background: linear-gradient(90deg, rgba(150,150,150,1) 60%, rgba(0,137,123,1) 60%);
  border-radius: 26px;
  box-shadow: 0px 0px 62px 3px #00897B;
    width: 60%;
    height: 55%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
}

.left_div {
  width: 60%;
  display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.right_div{
  width: 40%;
}


</style>