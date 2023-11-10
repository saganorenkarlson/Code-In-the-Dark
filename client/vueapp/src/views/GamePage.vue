
<template>
  
<div class="game" >
  <NavBar @click="handleClick"/>

  <transition name="fade" appear>
    <div class="modal-overlay" v-if=showModal @click="handletoFalse"></div>
   </transition>
   <transition name="slide" appear>
   <PopUpCard @handleClickNo="handletoFalse" @handleClickYes="handleClickYes" :showModal="showModal"/> 
   </transition>

  <div class="left_game_page" > 
    <div class="left_inner_div" id="tests" >
      
</div>
  </div>
  <div class="right_game_page"> 

    <textarea class="code_input"  ref="codeInput" v-model="code"></textarea>
    
    
  </div>

       
</div>
</template>

<script>
import NavBarGame from '../components/bars/NavBarGame.vue'
import axios from 'axios';
import PopUpCard from '@/components/cards/PopUpCard.vue';
import {useResultsStore} from '../stores/results.js'


export default {
name: 'GamePage',
components: {
    'NavBar': NavBarGame,
    'PopUpCard': PopUpCard,
  },
data() {
    return {
      results: [],
      showModal: false, 
    };
  },
  methods:{
    async handleClick(){
      this.showModal=true;
      console.log(this.showModal);
    },
    handletoFalse(){
      this.showModal=false;
      console.log(this.showModal);
    },
    async handleClickYes(){
      const store = useResultsStore();
      await store.updateResults(this.$refs.codeInput.value);
      this.$router.push("/profile");
    }
  },  


  async mounted() {
axios
    .get('http://localhost:8000/api/html')
    .then((response) => {
      var res= response.data.results[0].code;
      let newDiv = document.createElement("div");
      newDiv.innerHTML = res;
      document.getElementById("tests").appendChild(newDiv);
    })
    .catch((error) => {
      console.error(error);
    });
},

};

</script>

<script setup> 

</script>

<style> 

.game{
    width:100vw;
    height:100vh;
    display: flex;
    align-content: center;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    
}

.left_game_page{
width:50%;
height:100%;
background-color: #D9D9D9;
}

.right_game_page{
  width:50%;
height:100%;
}

.code_input{
  height: 82%;
    width: 90%;
    background: none;
    font-family: 'Cascadia Code', sans-serif;
    color: #fff;
    margin: 110px 10px 10px 10px;
    vertical-align: top;
    border: none;
  outline: none;
}

.left_inner_div{
  height: 82%;
    width: 90%;
    background: none;

    margin: 110px 10px 10px 10px;
}

.code_input:focus {
border: none;}

.modal-overlay {
 position: absolute;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 z-index: 98;
 background-color: rgba(0, 0, 0, 0.3);
}


</style>