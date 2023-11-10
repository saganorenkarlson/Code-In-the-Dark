<template>
  <div class="profile" >
    <NavBar/>
    <CardProfile :renderFull="renderFull">  
      <template  v-slot:left>
        <div class="profile-left-container" v-if="todaysResults !=null">
          <font-awesome-icon class="star-icon" :icon="['fas', 'star']" />
          <h1 class="profile-left-text">You have completed the challenge of today</h1>
          <ScoreBar :percentage="todaysResults"/>
          <p class="count-down-text">Show stats <span class="clickable-text" @click="$event => renderFull = true"> Here</span></p>
        </div>
        <div class="profile-left-container" v-else-if="isLoading">
          <p>Loading...</p>
        </div>
        <div class="profile-left-container" v-else>
          <h1 class="profile-left-text-begin">Challenge of the day</h1>
          <ButtonOverall label="Begin" @click="navigateToGame"/>
        </div>
  </template> 
  
  <template  v-slot:right>
      <p class="count-down-text">Next challenge in:</p>
      <CountDown></CountDown>
      <p class="count-down-text">Show previous days <router-link class="statistics-link" to="/statistics">
        here
        </router-link> </p>
  </template>

  <template v-if="renderFull" v-slot:full>
    <LeaderBoard @click="$event => renderFull = false"/>
  </template>
  
  </CardProfile>
  </div>
  </template>
  
  <script>
  import NavBar from '../components/bars/NavBar.vue'
  import CardProfile from '../components/cards/CardProfile.vue';
  import CountDown from '../components/countDowns/CountDown.vue'
  import ScoreBar from '../components/ScoreBar.vue'
  import ButtonOverall from '../components/buttons/ButtonOverall.vue'
  import LeaderBoard from '../components/LeaderBoard.vue'
  import {useResultsStore} from '../stores/results.js'
  export default {
  name: 'ProfilePage',
  components: {
      'NavBar': NavBar,
      'CardProfile': CardProfile,
      'CountDown': CountDown,
      'ScoreBar': ScoreBar,
      'ButtonOverall': ButtonOverall,
      'LeaderBoard': LeaderBoard,
    },
    computed: {
      todaysResults() {
        return useResultsStore().getTodaysResults
      }
    },
    data() {
    return { renderFull: false, isLoading: false }
  }, methods: {
    navigateToGame() {
      this.$router.push("/game");
    },

  },

  };

  </script>

  
  <style> 

  .profile{
      width:100vw;
      height:100vh;
      display: flex;
      align-content: center;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      
  }

  .count-down-text {
    font-size: 1.5rem;
  }
  .clickable-text {
    text-decoration: underline;
  }

  .clickable-text:hover{
    cursor: pointer;
  }

  .profile-left-text{
    font-size: 2rem;
    margin:3rem 1rem 0 1rem;
    font-weight: 300;

  }
  
  .profile-left-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    height: 100%;
    justify-content: center;
  }

  .star-icon {
    position: absolute;
    top:0;
    left:0;
    margin: 1rem;
    color:yellow;
  }

  </style>