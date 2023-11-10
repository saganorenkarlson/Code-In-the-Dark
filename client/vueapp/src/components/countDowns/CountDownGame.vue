<template>
    <div>
      <h1>{{ formattedTime }}</h1>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  
  export default {
    name: 'CountdownTimer',
    props: {
      onFinish: {
        type: Function,
        required: true
      }
    },
    setup(props) {
      const totalSeconds = ref(20 * 60);
      
      const formattedTime = computed(() => {
        const minutes = Math.floor(totalSeconds.value / 60);
        const seconds = totalSeconds.value % 60;
        return `${padZero(minutes)}:${padZero(seconds)}`;
      });
  
      const timer = setInterval(() => {
        totalSeconds.value--;
        if (totalSeconds.value === 0) {
          clearInterval(timer);
          props.onFinish(); // Call the onFinish function when the countdown reaches 0
        }
      }, 1000);
  
      return {
        formattedTime
      };
    }
  };
  
  function padZero(number) {
    return number.toString().padStart(2, '0');
  }
  </script>
  
  <style scoped>
  h1 {
    font-size: 3.8rem;
    font-weight: bold;
    margin: 0;
    color: #00897B;
  }
  </style>
  