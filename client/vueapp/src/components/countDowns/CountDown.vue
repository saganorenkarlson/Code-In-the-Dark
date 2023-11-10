<template>
    <div class="countdown-timer">
      <span class="countdown-timer__item" id="hour">{{ hours.toString().padStart(2, '0') }}</span>
      <span class="countdown-timer__separator">h</span>
      <span class="countdown-timer__item" id="minutes">{{ minutes.toString().padStart(2, '0') }}</span>
      <span class="countdown-timer__separator">m</span>
      <span class="countdown-timer__item" id="seconds">{{ seconds.toString().padStart(2, '0') }}</span>
      <span class="countdown-timer__separator">s</span>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        hours: 0,
        minutes: 0,
        seconds: 0,
        intervalId: null
      };
    },
    mounted() {
      // Start the countdown timer
      this.startCountdown();
    },
    beforeUnmount() {
      // Clear the interval before the component is destroyed
      clearInterval(this.intervalId);
    },
    methods: {
      startCountdown() {
        // Calculate the time remaining to the next 00.01 at night
        const now = new Date();
        const tomorrow = new Date(now);
        tomorrow.setDate(now.getDate() + 1);
        tomorrow.setHours(0);
        tomorrow.setMinutes(1);
        tomorrow.setSeconds(0);

        // Update the countdown timer every 100 milliseconds
        this.intervalId = setInterval(() => {
          const currentTime = new Date();
          const timeDifference = tomorrow - currentTime;
          this.hours = Math.floor(timeDifference / (1000 * 60 * 60));
          this.minutes = Math.floor(
            (timeDifference % (1000 * 60 * 60)) / (1000 * 60)
          );
          this.seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
        }, 100);
      }
    }
  };
  </script>
  
  <style scoped>
  .countdown-timer {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
  }
  
  .countdown-timer__item {
    font-size: 2rem;
  }
  
  .countdown-timer__separator {
    margin: 0px 15px 0px 0px;
    font-size: 2rem;
  }

  #hour{
    color:#E1E367;
  }
  #minutes{
    color: #543694;
  }
 #seconds{
color: #961281;
  }

  </style>
  