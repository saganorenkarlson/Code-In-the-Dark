<template>
<div class="month-selector">
    <font-awesome-icon class="month-arrow-icon" :icon="['fas', 'angle-left']" @click="decreaseMonth"/>
    <div class="month-text">{{ selectedMonth }}</div>
    <font-awesome-icon :class="['month-arrow-icon', {'month-arrow-icon-hidden': selectedMonthNr >= currentMonthNr && selectedYear >= currentYear}]"  :icon="['fas', 'angle-right']" @click="increaseMonth"/>
</div>
</template>
    
<style>
@import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');

.month-selector {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 2rem;
  }

  .month-selector .svg-inline--fa {
    height: 1.5rem;
  }

  .month-arrow-icon {
    margin: 1rem;
    cursor: pointer;
  }

  .month-arrow-icon-hidden {
    visibility: hidden;
  }

  .month-text {
    width: 11rem;
    background-color: black;
    height: 2.7rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    font-weight: 200;
    border-radius: 2rem;
    font-family: Inconsolata;
  }
</style>
      
      
<script>  
export default {
    name: 'MonthSelector',
    props: ['selectedMonthNr','selectedYear'],
    data() {
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    return {
      monthNames: [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ],
      currentMonthNr: currentMonth,
      currentYear: currentYear,
    };
    },
    computed: {
      selectedMonth() {
        return this.monthNames[this.selectedMonthNr];
      }
    },
    methods: {
      increaseMonth(){
        let updatedSelectedMonthNr = this.selectedMonthNr;
        let updatedSelectedYear = this.selectedYear;
        if(this.selectedMonthNr != 11) {
          updatedSelectedMonthNr = this.selectedMonthNr + 1;
        } else {
          updatedSelectedMonthNr = 0;
          updatedSelectedYear = this.selectedYear + 1;
        }
        this.$emit("updateSelectedDate", updatedSelectedMonthNr, updatedSelectedYear);
      },
      decreaseMonth() {
        let updatedSelectedMonthNr = this.selectedMonthNr;
        let updatedSelectedYear = this.selectedYear;
        if(this.selectedMonthNr != 0) {
          updatedSelectedMonthNr = this.selectedMonthNr - 1;
        } else {
          updatedSelectedMonthNr = 11;
          updatedSelectedYear = this.selectedYear -1;
        }
        this.$emit("updateSelectedDate", updatedSelectedMonthNr, updatedSelectedYear);
      }
    }
}
</script>