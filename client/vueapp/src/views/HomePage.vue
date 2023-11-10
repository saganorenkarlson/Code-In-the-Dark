
<template>
    <div class="home"  @mousemove="onMouseMove">
      <div class="flashlight" :style="{ left: mouseX + 'px', top: mouseY + 'px' }">
      <div class="flashlight-mask"></div>
    </div>
    <div id="div_to_hover" >
      
    <div id="div_to_dissapear" > 
      </div> 
    <h1 id="code"> Code</h1>
    <h1 id="in_the"> in the</h1>
    <h1 id="dark"> DARK</h1>
    <my-button label="Begin" @click="handleClick"> </my-button>
  </div>

  </div>
</template>


<script setup>
import { useRouter } from "vue-router";
import { getAuth, onAuthStateChanged } from "firebase/auth";

const router = useRouter();
const handleClick =() => {

const auth = getAuth();
onAuthStateChanged(auth, (user) => {
if (user) {
    router.push('/profile');
} else {
    router.push('/sign-in');
}
})}

</script>

<script>
import ButtonBegin from '../components/buttons/ButtonBegin.vue'


export default {
  name: 'HomePage',
  components: {
    'my-button': ButtonBegin
  },
  data() {
    return {
      mouseX: 0,
      mouseY: 0,
    };
  },
  methods: {
    onMouseMove(event) {
      if(event.pageX > window.innerWidth-100){
        this.mouseX = window.innerWidth-100
      }
      else{
      this.mouseX = event.pageX;
      }

    if(event.pageY > window.innerHeight-101){
    this.mouseY =window.innerHeight-101
    }
    else{
      
      this.mouseY = event.pageY;
    }
  },
   },
  }

</script>



<style>

.home{
    background-color: #363636;
    width:100vw;
    height:100vh;
    display: flex;
    align-content: center;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    overflow: hidden; 
}

  #div_to_hover{
    display: flex;
    position: relative;
    align-content: center;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-right: 4rem;
    margin-left: 4rem;
    padding-right: 4rem;
    padding-left: 4rem;
    height: 60rem;
    background-color: #363636;
    overflow: hidden; 
  }


#div_to_dissapear{
  position: absolute;
    height: 33rem;
    width: 110%;
    background-color: #363636;
    opacity: 1;
    top: 0;
    
}

#div_to_dissapear:hover{
  opacity: 0;
  z-index: 1;
}

  .flashlight {
  position: absolute;
  width: 200px;
  height: 200px;
  border-radius: 100%;
  background-color: rgba(250, 255, 97, 0.729);
  z-index: 999;
  pointer-events: none;
  transform: translate(-50%, -50%);
  box-shadow: 0px 0px 100px #f1ff76;
}

.flashlight-mask {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: 100%;
  background-color: rgb(129, 135, 81);
  pointer-events: none;
  -webkit-mask-image: radial-gradient(circle at center, transparent 0%, transparent 20%, rgb(169, 0, 0) 100%);
  mask-image: radial-gradient(circle at center, transparent 0%, transparent 20%, black 100%);
}


#code{
    letter-spacing: 0.1em;
    -webkit-text-fill-color: #363636; /* Will override color (regardless of order) */
    -webkit-text-stroke-width: 1px;
    font-style: normal;
    font-size: 10rem;
    -webkit-text-stroke-color: #00897B;
    text-shadow: 0px 0px 24px #00897B;
    margin: 0;
}

#in_the{
    color: #00897B;
    font-size: 5rem;
    margin: 0;
    text-shadow: 0px 0px 24px #00897B;
}

#dark{
    color: #00897B;
    font-size: 10rem;
    margin: 0;
    text-shadow: 0px 0px 24px #00897B;
    font-weight: bold;
}


</style>


