<template>
<div class="score-container">
    <p class="score-text">Score:</p>
    <div class="progress-bar-container">
      <div class="progress-bar" :style="style"></div>
    </div>
    <p class="score-text">{{percentage}}%</p>
</div>
</template>
  
  <script>
  export default {
    props: ['percentage'],
    computed: {
      style () {
        return 'width: ' + this.percentage + '%';
      }
    },
  };
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');

  .progress-bar-container {
    height: 40px;
    width: 249px;
    background-color: #969696;
    border-radius: 2rem;
    overflow: hidden;
    margin: 1rem;
  }
  
  .progress-bar {
    height: 100%;
    background-color: #00564D;
    border-radius: 2rem;
  }

  .score-container{
    display: flex;
    align-items: center;  
    margin: 1rem;
  }

  .score-text {
    font-size: 1.5rem;
    font-family: Inconsolata;
    color: white;
  }

  </style>