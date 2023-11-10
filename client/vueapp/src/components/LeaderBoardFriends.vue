<template>
    <div class="leaderboard-friends-wrapper">
        <h3 class="leaderboard-friends-title">Top three among your friends this month</h3>
        <div class="leaderboard-friends-text-wrapper" v-for="(result,index) in filteredResultsFriendsAverage" :key="result.username">
            <h3 class="leaderboard-friends-text" id="left-text">{{index +1 }}. <span :style="{color: (result.username == 'You') ? '#E910C6' : 'white' }">{{ result.username }}</span> </h3>
            <h3 class="leaderboard-friends-text"> Average score: {{ result.averagePercentage }}%</h3> 
        </div>
        <div v-for="i in (3 - filteredResultsFriendsAverage.length > 0) ? 3 - filteredResultsFriendsAverage.length : 0" :key="i">
            <h3 class="leaderboard-friends-text">{{ filteredResultsFriendsAverage.length + i }}. -</h3>
          </div>
    </div>
    </template>
            
    <style>
    @import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');
    
    .leaderboard-friends-wrapper {
        width:fit-content;
    }
    .leaderboard-friends-title {    
        font-family: Inconsolata;
        color: #00897B;
        font-size: 2rem;
        margin: 0 0 0.7rem 0;
    }

    .leaderboard-friends-text {
        color: white;
        text-align: left;
        font-weight: 200;
        width:15rem;
        margin:0.2rem 0 0.2rem 0.2rem;
    }

    #left-text{
        flex-grow: 1;
    }

    .leaderboard-friends-text-wrapper {
        display: flex;
        justify-content: space-between;
    }
    </style>
                    
    <script>       
        export default {
            name: 'LeaderBoardFriends',
            props: ['filteredFriends','filteredResults','dayCount'],
            computed: {
                filteredResultsFriendsAverage () {
                    const filteredFriends = [...this.filteredFriends, {
                        username: 'You',
                        results: this.filteredResults
                    }]
                    const defaultValue = 0;
                    return filteredFriends.map(friend => {
                        const percentages = friend.results.map(result => result.percentage)
                        const averagePercentage =  percentages.length > 0 ? (percentages.reduce((acc, curr) => parseFloat(acc) + parseFloat(curr), 0.0) / this.dayCount).toFixed(2) : defaultValue.toFixed(2) ;
                        return {
                            username: friend.username,
                            averagePercentage: averagePercentage
                        };

                    }).sort((a, b) => b.averagePercentage - a.averagePercentage).slice(0,3);
                }
            }
        }
    </script>