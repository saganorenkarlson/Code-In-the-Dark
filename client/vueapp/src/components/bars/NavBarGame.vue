<template>
    <div class="nav-bar">
        <div class="fill_div"> </div>

        <CountDownGame> </CountDownGame>
    
<ButtonFinish label="Finish" @click="handleClick"> </ButtonFinish>


    </div>
</template>

<style>

.fill_div{
    
    width: 271px;
}
.nav-bar {
    background-color: black;
    display: flex;
    height: 6rem;
    flex-direction: row;
    align-content: stretch;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    top: 0;
    width: 100%;
}

.nav-bar-text {
    margin-left: 1rem;
    color: #00897B;
    font-size: 3.5rem;
}

.nav-bar-icon {
    font-size: 3rem;
    margin: 1rem;
}


.nav-options {
    display: flex;
    flex-direction: row;
    width: 11rem;
    justify-content: space-between;
}

.nav-option-wrapper {
    border-radius: 1rem;
    width: 5rem;
    display: flex;
    justify-content: center;
}

.nav-option-wrapper:hover {
    background-color: #363636;
}

</style>
  
<script>  
import CountDownGame from "../countDowns/CountDownGame.vue";
import ButtonFinish from "../buttons/ButtonFinish.vue";


    export default {
    name: 'NavBarGame',
    components: {
    'CountDownGame': CountDownGame,
    'ButtonFinish': ButtonFinish,

  },
  props:['handleClick']
    }
</script>
