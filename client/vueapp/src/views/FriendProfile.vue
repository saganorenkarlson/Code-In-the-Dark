<template>
    <NavBar/>
    <div class="friend-profile-upper-wrapper">
        <div class="friend-title">
                <font-awesome-icon class="friend-arrow-icon" :icon="['fas', 'angle-left']" @click="goBack"/>
                <span class="username-style">{{this.username}}</span>'s results this month
        </div>
        
        <div class="friend-profile-upper-content-wrapper">
        <StatisticsList :filteredResults="filteredResults" :noResults="false" :errorMsg="false" :personalResults="false"/>
        <StatisticsGraph :filteredResults="filteredResults" :errorMsg="false" :daysInMonth="daysInMonth"/>
        </div>
    </div>
    <div class="friend-profile-lower-wrapper"> 
        <ButtonOverall :label="friendStatus" @click="handleFriendStatusChange"/>
    </div>
</template>
  
<style>
@import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');

.friend-profile-upper-wrapper {
    margin-top: 7rem;
    color: white;
    width: 100%;
  }

.friend-profile-upper-content-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

.friend-profile-lower-wrapper{
    margin-top:2rem;
    display: flex;
    justify-content: center;
}

.friend-title{
    height: 56px;
    margin-bottom: 2rem;
    font-size: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
}
  
.username-style{
    color: #E910C6;
}
  
.friend-arrow-icon{
    margin-right: 2rem;
}

.friend-arrow-icon:hover{
    cursor: pointer;
}

.friend-title .svg-inline--fa{
    height: 2rem;
}

</style>
  
<script>  
  import NavBar from "../components/bars/NavBar.vue"
  import StatisticsList from "@/components/StatisticsList.vue";
  import StastisticsGraph from "@/components/StastisticsGraph.vue";
  import ButtonOverall from "@/components/buttons/ButtonOverall.vue"; 

  import {getCurrentUser} from '../router/index.js';
  import {useResultsStore} from '../stores/results.js'
  import axios from "axios";


  export default {
    name: 'FriendProfile',
    components: {
        'NavBar': NavBar,
        'StatisticsList': StatisticsList,
        'StatisticsGraph': StastisticsGraph,
        'ButtonOverall': ButtonOverall,
    },
    data() {
        const currentDate = new Date();
        const currentMonth = currentDate.getMonth();
        const daysInMonth = new Date(new Date().getFullYear(), currentMonth + 1, 0).getDate();
        return {
            username: '',
            daysInMonth: daysInMonth,
            filteredResults: [],
        };
    },
    async mounted(){
        this.username = this.$route.params.username;
        const user = await getCurrentUser();
        const token = await user.getIdToken();
        const name = user.email;
        const config = {
        headers: { Authorization: `Bearer ${token}` },
        params: {
            requesting_user: name,
            target_user: this.username,
        }
        };

        try {
        const response = await axios.get('http://localhost:8000/api/user-results', config);
        this.filteredResults = response.data.results;
        } catch (error) {
        this.errorMsg = error.message;
        }

        const store = useResultsStore();
        await store.fetchFriends();
        await store.fetchRequests();      
    },
    computed: {
        friendStatus(){
            const currentFriend = useResultsStore().getFriends.some(friend => friend.username == this.username)
            const requestReceived = useResultsStore().getRequestsReceived.some(friend => friend.username == this.username)
            const requestSent = useResultsStore().getRequestsSent.some(friend => friend.username == this.username)
            if(currentFriend) {
                return "Remove friend";
            } else if(requestReceived) {
                return "Accept friend request";
            } else if(requestSent) {
                return "A friend request has been sent";
            } else {
                return "Add friend";
            }
        }
    },
    methods:{
        goBack(){
            this.$router.push("/friends");
        },
        handleFriendStatusChange(){
            const store = useResultsStore();
            switch(this.friendStatus){
                case 'Remove friend':
                    store.removeFriend(this.username)
                    break;
                case 'Accept friend request':
                    store.answerRequest(this.username,true);
                    break;
                case 'A friend request has been sent':
                    break;
                case 'Add friend':
                    store.sendRequest(this.username);
                    break;
                default:
                    break;
            }
        }
    },
  };
</script>
  