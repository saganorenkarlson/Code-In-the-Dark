<template>
    <div class="wrapper-box">
      <slot></slot>
    </div>
</template>

<style>
.wrapper-box{
    width: 29rem;
    height: 17rem;
    background-color: #D9D9D9;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 1.7rem;
    font-family: Inconsolata;
    box-shadow: 0px 0px 62px 3px #00897B;
    margin: 0 3rem 0 3rem;
}
</style>

<script>  
  export default {
    name: 'WrapperBox'
  };
</script>