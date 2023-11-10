import { defineStore } from 'pinia'
import axios from "axios"
import {getCurrentUser} from '../router/index.js';


export const useResultsStore = defineStore("results",{
    state: () => ({
        results : [],
        errorMsg: '',
        friends : [],
        leaderboard : [],
        requestsSent: [],
        requestsReceived: [],
    }),
    persist: true,
    getters: {
        getErrorMsg(state) {
          return state.errorMsg
        },
        getResults(state) {
            return state.results
        },
        getFriends(state) {
          return state.friends;
        },
        getTodaysResults(state) {
            const todaysResult= state.results.find(result => {
                const date = new Date(result.date);
                const currentDate = new Date();
                return (date.getFullYear() == currentDate.getFullYear() && date.getMonth() == currentDate.getMonth() && date.getDate() == currentDate.getDate())
              });
            return todaysResult ? todaysResult.percentage : null;
        },
        getRequestsSent(state){
          return state.requestsSent;
        },
        getRequestsReceived(state){
          return state.requestsReceived;
        },
    },
    actions: {
        async fetchResults(){

              const user = await getCurrentUser();
              console.log(user)
              const token = await user.getIdToken();
              const name = user.email;
              const config = {
                headers: { Authorization: `Bearer ${token}` },
                params: {
                username: name
              }
              };
      
              try {
                const response = await axios.get('http://localhost:8000/api/user', config);

                this.results = response.data.results;
                this.errorMsg = '';
              } catch (error) {
                this.errorMsg = error.message;
              }
        }, async fetchFriends(){
          const user = await getCurrentUser();
          const token = await user.getIdToken();
            const name = user.email;
            const config = {
              headers: { Authorization: `Bearer ${token}` },
              params: {
              username: name
            }
            };
    
            try {
              const response = await axios.get('http://localhost:8000/api/friends', config);
              this.friends = response.data.friends;
              this.errorMsg = '';
            } catch (error) {
              this.errorMsg = error.message;
            }
      }, 
        async fetchLeaderBoard(){
              axios
                .get('http://localhost:8000/api/top')
                .then((response) => {
                  this.leaderboard = response.data.results;
                  this.errorMsg = '';
                })
                .catch((error) => {
                  this.errorMsg = error.message;
                });
        },
        async updateResults(result){
          const user = await getCurrentUser();
          const token = await user.getIdToken();
          const name = user.email;
          const config = {
            headers: { Authorization: `Bearer ${token}` },
            params: {
              username: name,
              result: result
            },
          };

          try {
            const response = await axios.put('http://localhost:8000/api/user/', {}, config);
            this.results = response.data.results;
            this.errorMsg = '';
          } catch (error) {
            this.errorMsg = error.message;
          }
      }, 
      async newUser() {
        const user = await getCurrentUser();
          const token = await user.getIdToken();
          const name = user.email;
          const config = {
            headers: { Authorization: `Bearer ${token}` },
            params: {
              username: name,
            },
          };

          try {
            await axios.post('http://localhost:8000/api/user/', {}, config);
            this.errorMsg = '';
          } catch (error) {
            this.errorMsg = error.message;
          }

      },
      reset() {
        this.results = []
        this.errorMsg= ''
        this.friends= []
        this.leaderboard = []
        this.requestsReceivedd = []
        this.requestsSent = []  
      },
      async fetchRequests(){
        const user = await getCurrentUser();
        const token = await user.getIdToken();
        const name = user.email;
        const config = {
          headers: { Authorization: `Bearer ${token}` },
          params: {
          username: name
        }
        };

        try {
          const response = await axios.get('http://localhost:8000/api/friends/requests', config);
          this.requestsReceived = response.data.requests_received;
          this.requestsSent = response.data.requests_sent;
          this.errorMsg = '';
        } catch (error) {
          this.errorMsg = error.message;
        }
      },
      async sendRequest(target_user){
        const user = await getCurrentUser();
        const token = await user.getIdToken();
        const name = user.email;
        const config = {
          headers: { Authorization: `Bearer ${token}` },
          params: {
            requesting_user: name,
            target_user: target_user,
          },
        };

        try {
          const response = await axios.post('http://localhost:8000/api/friends/requests', {}, config);
          this.requestsSent = response.data.requests_sent;      
          this.errorMsg = '';  
        } catch (error) {
          this.errorMsg = error.message;
        }
      },
      async answerRequest(requesting_user,answer){
        const user = await getCurrentUser();
        const token = await user.getIdToken();
        const name = user.email;
        const config = {
          headers: { Authorization: `Bearer ${token}` },
          params: {
            answering_user: name,
            requesting_user: requesting_user,
            answer: answer,
          },
        };
        try {
          const response = await axios.put('http://localhost:8000/api/friends/requests', {}, config);
          this.friends = response.data.friends;
          this.requestsReceived = response.data.requests_received;    
          this.errorMsg = '';    
        } catch (error) {
          this.errorMsg = error.message;
        }
      },
      async removeFriend(target_username){
        const user = await getCurrentUser();
        const token = await user.getIdToken();
        const name = user.email;
        const config = {
          headers: { Authorization: `Bearer ${token}` },
          params: {
            username: name,
            target_username: target_username,
          },
        };
        try {
          const response = await axios.delete('http://localhost:8000/api/friends', config);
          this.friends = response.data.friends;
          this.errorMsg = '';
        } catch (error) {
          this.errorMsg = error.message;
        }
      },
    },
})