  <template>
    <NavBar/>
    <div class="statistics-page-upper-wrapper">
      <MonthSelector :selected-month-nr="selectedMonthNr" :selected-year="selectedYear" @updateSelectedDate="(newSelectedMonthNr, newSelectedYear) => {
        selectedMonthNr = newSelectedMonthNr;
        selectedYear = newSelectedYear;
      }" ></MonthSelector>
    <div class="statistics-page-upper-content-wrapper">
        <StatisticsList :filteredResults="filteredResults" :noResults="noResults" :errorMsg="errorMsg" :personalResults="true"/>
        <StastisticsGraph :filteredResults="filteredResults" :errorMsg="errorMsg" :daysInMonth="daysInMonth"/>
      </div>
    </div>
    <div class="statistics-page-lower-wrapper">
      <LeaderBoardFriends :filteredFriends="filteredFriends" :filteredResults="filteredResults" :dayCount="dayCount" ></LeaderBoardFriends>
    </div>
  </template>
    
  <style>
  .statistics-page-upper-wrapper {
    margin-top: 7rem;
    color: white;
    width: 100%;
  }

  .statistics-page-upper-content-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  .statistics-page-lower-wrapper{
    margin-top:2rem;
    display: flex;
    justify-content: center;
  }

  </style>
    
  <script>
  import NavBar from "../components/bars/NavBar.vue"
  import MonthSelector from '@/components/MonthSelector.vue';
  import StatisticsList from '@/components/StatisticsList.vue';
  import LeaderBoardFriends from "@/components/LeaderBoardFriends.vue";
  import StastisticsGraph from "@/components/StastisticsGraph.vue"
  import {useResultsStore} from '../stores/results.js'

  export default {
      name: 'StatisticsPage',
      components: {
        'NavBar': NavBar,
        'MonthSelector': MonthSelector,
        'StatisticsList': StatisticsList,
        'LeaderBoardFriends': LeaderBoardFriends,
        'StastisticsGraph': StastisticsGraph
      },
      async mounted() {
      const store = useResultsStore();

      if (store.getFriends.length == 0) {
      await store.fetchFriends();
      }

      },
    data() {
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    return {
      selectedMonthNr: currentMonth,
      selectedYear: currentYear,
    };
    },
      computed: {
      errorMsg() {
        return useResultsStore().getErrorMsg;
      },
      filteredResults() {
        return useResultsStore().getResults.filter(result => {
          const date = new Date(result.date);
          return date.getMonth() == this.selectedMonthNr && date.getFullYear() == this.selectedYear;
        });
      },
      filteredFriends() {
        const filteredFriends = useResultsStore().getFriends.map((friend) => {
        const filteredResults = friend.results.filter(result => {
        const date = new Date(result.date);
        return date.getMonth() == this.selectedMonthNr && date.getFullYear() == this.selectedYear;
        });
        return {
          ...friend,
          results: filteredResults
        };
        });

        return filteredFriends;
        },
        daysInMonth () {
          return new Date(new Date().getFullYear(), this.selectedMonthNr + 1, 0).getDate();
        },
        dayCount() {
          const currentDate = new Date();
          const currentMonth = currentDate.getMonth();
          const currentYear = currentDate.getFullYear();          
          return (currentYear == this.selectedYear && currentMonth == this.selectedMonthNr) ? currentDate.getDate() : this.daysInMonth;      
        },
        noResults(){
          return useResultsStore().getResults.length == 0;     
        }
      
    },
    };
  </script>
    






