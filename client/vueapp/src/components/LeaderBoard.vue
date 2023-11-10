<template>
  <div class="leaderboard-container">
  <font-awesome-icon class="arrow-icon" id="arrow" :icon="['fas', 'arrow-left']" @click="onClick" size="lg"/>
  <h1 class="leaderboard-title">Leaderboard</h1>
  <div class="leaderboard-text-container" v-for="(leader,index) in leaderboard" :key="leader.username">
    <h3 class="leaderboard-text">
      <font-awesome-icon v-if="index <3" class="leaderboard-icon" :icon="['fas', 'medal']"  :style="{ color: index == 0 ? 'gold' : index == 1 ? '#9B9B9A' : '#E27022' }"/>
      {{index + 1}}. {{ leader.username }} {{ leader.percentage }}%</h3> 
  </div>
  <div class="leaderboard-text-container" v-for="i in 5 - leaderboard.length" :key="i">
    <h3 class="leaderboard-text">{{ leaderboard.length + i }}. -</h3>
  </div>
  </div>
</template>
      
<script>
  import {useResultsStore} from '../stores/results.js'

  export default {
  name: 'LeaderBoard',
  props: [],
  methods: {
    onClick() {
      this.$emit('onClick');
    }
  },
  async mounted() {
    const store = useResultsStore();
    await store.fetchLeaderBoard();
  },
  computed: {
    leaderboard() {
      return useResultsStore().leaderboard
    }
  },

  };
</script>
      
<style>
@import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');

.leaderboard-title{
    font-size: 3.5rem;
    font-family: Inconsolata;
    font-weight: 300;
    margin:1.5rem 0 1.5rem 0;
  }

  .leaderboard-text {
    font-size: 2rem;
    margin:1rem 0 0 0;
    font-family: Inconsolata;
    font-weight: 200;
    position: relative;
  }

  .leaderboard-text-container{
    width: 65%;
    margin: 0 auto 0 auto;
    text-align: left;
  }

.leaderboard-icon{
  position: absolute;
  left:-3rem;
  padding-top:0.2rem;
  border:black;
}

.leaderboard-text .svg-inline--fa{
  height: 2rem;
}

.arrow-icon {
  margin: 1.5rem;
  position:absolute;
  top: 0;
}
.arrow-icon:hover {
  cursor: pointer;
}

.svg-inline--fa  {
  height: 3.5rem;
}

.leaderboard-container {
  width:100%;
  height: 100%;
  position: relative;
  display:flex;
  flex-direction: column;
}

</style>