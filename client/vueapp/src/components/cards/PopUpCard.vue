<template>
        <div class="modal" v-if=showModal>
     <h1>Are you sure you want to finish?</h1>

     <div class="buttonPopup"> 
     <ButtonOverall @customClick="handleClickYes" label="Yes"/>  
     <ButtonOverall @click="handleClickNo" label="No"/>
    </div>
<p> There is no second chance on todays challenge</p>
    </div>

  </template>
  
  <script>
  import ButtonOverall from '../buttons/ButtonOverall.vue';

export default {
    name: "PopUpCard",
    props: [ "showModal"],
    methods: {
      handleClickYes() {
            this.$emit("handleClickYes");
        },
        handleClickNo(){
          
          this.$emit("handleClickNo");
        }
    },
    components: { ButtonOverall }
}


  </script>


<style>

.wrapper-div {
  height: 100%;
  width: 100%;
  display:flex;
  align-items: center;
}


.modal {
 position: fixed;
 top: 50%;
 left: 50%;
 transform: translate(-50%, -50%);
 z-index: 99;
 width: 100%;
 max-width: 500px;
 padding: 25px;
 background-color:#969696;
  box-shadow: 0px 0px 62px 3px #00897B;
  height: 45%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    flex-direction: column;
}
 
.modal h1{
  color: #fff;
  font-size: 28px;
  font-weight: 300;
  margin-bottom: 15px;
 }
 
 .modal p {
  color: #fff;
  font-size: 15px;
  font-weight: 300;
  margin-bottom: 15px;
 }


.fade-enter-active,
.fade-leave-active {
 transition: opacity .5s;
}

.fade-enter,
.fade-leave-to {
 opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
 transition: transform .5s;
}

.slide-enter,
.slide-leave-to {
 transform: translateY(-50%) translateX(100vw);
}

.buttonPopup{    display: flex;
    width: 78%;
    justify-content: space-evenly;
}
</style>