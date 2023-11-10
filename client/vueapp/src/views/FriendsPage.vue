<template>
    <NavBar/>
    <div class="friend_page_wrapper"> 
    <div class="friends-page-upper-wrapper">
        <div class="friends-page-upper-content-wrapper">
            <WrapperBox>
            <h4 class="friends-title" >Your friends</h4>
            <div class="friends-list-scrollable">
            <div class="friend" v-for="friend in friends" :key="friend.username">
                <router-link class="friend-link" :to="'/friends/' + friend.username">
                    <h3 class="friend-username">{{ friend.username }}</h3>
                  </router-link>            
            </div>
            <h3 class="template-text" v-if="friends.length == 0 && !errorMsg">You currently have no friends. Search for new friends in the search bar to the right!</h3>
            <h4 style="color:red; text-align: left" v-if="errorMsg">{{errorMsg }}</h4>
            </div>
            </WrapperBox>
            <WrapperBox>
            <h4 class="friends-title" >Search Users</h4>
              
    <SearchBar :handleSearch="handleSearch" />

    <div class="friends-list-scrollable">
      <div class="friend-request" v-for="SResults in searchResults.results" :key="SResults">
<router-link class="friend-link" :to="'/friends/' + SResults">
    <h3 class="friend-username">{{ SResults }}</h3>
  </router-link>            
</div> 
</div>  
            </WrapperBox>
        </div>
    </div>
    <div class="friends-page-lower-wrapper">

      <div class="fried_requests_div"> 
        <h4 class="friends-title">Friend requests </h4>
        <div class="friends-list-scrollable">
         <div class="friend-request" v-for="request in friendRequests" :key="request.username">
          <h3 class="friend-username">{{ request.username }}</h3> 
          <div class="icon-wrapper">
            <div class="answer-request-icon" id="check" @click="acceptRequest(request.username)">
                <font-awesome-icon :icon="['fas', 'check']" />
            </div> 
            <div class="answer-request-icon" id="cross" @click="declineRequest(request.username)">
                <font-awesome-icon :icon="['fas', 'x']" />
            </div>
          </div>
         </div>
         <h3 class="template-text" v-if="friendRequests.length == 0">No friend requests to show</h3>
      </div>
      </div>


    </div>
  </div>
</template>
  
<style>
@import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');

  
.friends-page-upper-wrapper {
    color: white;
    width: 100%;
}

.friends-page-upper-content-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.friends-page-lower-wrapper{
    margin-top:2rem;
    display: flex;
    justify-content: center;
}

.friends-title{
    margin: 0 0 0.5rem 0;
    color: #00897B;
    font-size: 2rem;
    font-family: Inconsolata;
}
  
.friend-username{
    margin:0;
    color: black;
    font-size: 1.5rem;
    line-height: 2rem;
    font-family: Inconsolata;

}

.icon-wrapper{
    display: flex;
}
.answer-request-icon{
    width:2rem;
    height: 100%;
    margin: 0 0.3rem;
    display: flex;
    align-content: center;
    justify-content: center;
    border-radius: 0.2rem;
    align-items: center;
}

#check{
    color: #00897B;
}

#cross {
    color: #E910C6;
}

.answer-request-icon:hover{
    background-color:#e3e3e3;
    cursor: pointer;
}

.answer-request-icon .svg-inline--fa{
    height: 1.7rem;
}

.friend-request{
    width: 100%;
    text-align: left;
    display: flex;
    justify-content: space-between;
}

.template-text{
    font-weight: 300;
    text-align: left;
    margin:0;
    color: black;
    font-family: Inconsolata;

}
.friend{
    width: 100%;
    text-align: left;
}

.friend:hover{
    background-color:#e3e3e3;
    cursor: pointer;
}

.friend-link{
    text-decoration: none;
}

.friends-list-scrollable::-webkit-scrollbar {
    width: 15px;
    margin-top:0.2rem;
}

.friends-list-scrollable::-webkit-scrollbar-track {
    background: #f1f1f1; 
}

.friends-list-scrollable::-webkit-scrollbar-thumb {
    background: #888; 
    height: 2rem;
}


.friends-list-scrollable{
    overflow-y: auto;
    height: 100%;
    width: 100%;
    margin-top:0.3rem;
}

.fried_requests_div{
  height: 120px;
    width: 38.3rem;
    background-color: #D9D9D9;
    box-shadow: 0px 0px 62px 3px #00897B;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 1.7rem;
}

.friend_page_wrapper{
  display: flex;
    width: 100%;
    height: 100%;
    margin-top: 150px;
    flex-direction: column;
    justify-content: space-evenly;
}
</style>
  
<script>  
  import NavBar from "../components/bars/NavBar.vue"
  import WrapperBox from "@/components/WrapperBox.vue";
  import {useResultsStore} from '../stores/results.js'
  import SearchBar from '../components/SearchBar.vue';
  import axios from "axios";
  import {getCurrentUser} from '../router/index.js';


  export default {
    name: 'FriendsPage',
    components: {
        'NavBar': NavBar,
        'WrapperBox': WrapperBox,
        'SearchBar': SearchBar
    }, 
    async mounted() {
      const store = useResultsStore();
      await store.fetchFriends();
      await store.fetchRequests();      
    },
    computed: {
        errorMsg() {
            return useResultsStore().getErrorMsg;
        },
        friends() {
            return useResultsStore().getFriends;
        },
        friendRequests() {
            return useResultsStore().getRequestsReceived;
        }
    },
    data() {
    return {
      searchQuery: '',
      searchResults: []
    };
  },
    methods: {
    async handleSearch(query) {
      this.searchQuery=query;
      const user = await getCurrentUser();
          const token = await user.getIdToken();
          const name = user.email;

            const config = {
              headers: { Authorization: `Bearer ${token}` },
              params: {
              searchQuery: this.searchQuery,
              username: name
            }
            };
            try {
              console.log(this.searchQuery)
              const response = await axios.get('http://localhost:8000/api/search', config);
              console.log(response.data)
              this.searchResults = response.data;

            } catch (error) {
              this.errorMsg = error.message;
            }
    },
    acceptRequest(username){
        useResultsStore().answerRequest(username,true);
    },
    declineRequest(username){
        useResultsStore().answerRequest(username,false);
    }
    }
    
    
  };
</script>
  
