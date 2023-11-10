<template>
    <div class="card" id="card_profile-full" v-if="renderFull"> 

        <slot name="full"></slot>
      
    </div>

    <div class="card" id="card_profile" v-else> 
    <div class="wrapper-div">
      <div class="left_div" id="left_profile">
        <slot name="left"></slot>
      </div>

      <div class="right_div" id="right_profile">
        <slot name="right"></slot>
      </div>
    </div>
  </div>

  </template>
  
  <script>
  
export default {
  name: 'card-profile',
  props: ['label','renderFull'],
      methods: {
        onClick() {
          this.$emit('click');
        }
  },
}


  </script>


<style>



#card_profile{
    background: rgb(150,150,150);
  background: linear-gradient(90deg,  rgba(0,137,123,1) 50%,rgba(150,150,150,1) 50%);
  margin-top: 2rem;
}

#card_profile-full {
  background: rgba(0,137,123,1);
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
}
#left_profile{
    width: 50%;
    height: 100%;
}
#right_profile{
    width: 50%;
}

.wrapper-div {
  height: 100%;
  width: 100%;
  display:flex;
  align-items: center;
}


</style>