<template>
<div class="statistics-list">
    <h3 class="statistics-list-title">{{personalResults ? 'Your' : 'The' }} statistics</h3>
    <div class="statistics-list-scrollable">
    <h4 style="color:red; text-align: left" v-if="errorMsg">{{errorMsg }}</h4>
    <div class="statistics-list-content-wrapper" v-for="result in filteredResults" :key="result.date">
        <h3 class="statistics-list-content">{{ result.date }}: &emsp; &emsp;{{ result.percentage }}%</h3> 
        <font-awesome-icon v-if="result.percentage > 80" :icon="['fas', 'star']" />
    </div>
    <h4 class="statistics-no-results" v-if="noResults && !errorMsg"> No results yet to show. Play 
        <router-link class="statistics-link" to="/profile">
            <span v-on:click="active = false">the game of today</span>
            </router-link> 
        and your results will be displayed here.
    </h4>
    </div>
</div>
</template>
        
<style>
@import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald');

.statistics-list {
    width: 29rem;
    height: 17rem;
    background-color: #D9D9D9;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 1.7rem;
    font-family: Inconsolata;
    box-shadow: 0px 0px 62px 3px #00897B;
    margin: 0 3rem 0 3rem;
}

.statistics-list-title{
    margin: 0 0 0.5rem 0;
    color: #00897B;
    font-size: 2rem;
}

.statistics-list-content{
    color: black;
    font-size: 1.5rem;
    margin: 0 0.5rem 0.3rem 0;
    text-align: left;
}

.statistics-list-scrollable{
    overflow-y: auto;
    height: 100%;
    width: 100%;
    margin-top:0.3rem;
}

.statistics-list-content-wrapper {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
}

.statistics-list-content-wrapper .svg-inline--fa {
    height: 1.2rem;
    color: yellow;
    margin:0 0.5rem 0.3rem 0;
}
.statistics-list-scrollable::-webkit-scrollbar {
    width: 15px;
    margin-top:0.2rem;
}

.statistics-list-scrollable::-webkit-scrollbar-track {
    background: #f1f1f1; 

}

.statistics-list-scrollable::-webkit-scrollbar-thumb {
    background: #888; 
    height: 2rem;
}

.statistics-no-results{
    margin: 0;
    color: black;
    font-weight: 300;
    text-align: left;
}

.statistics-link {
    color: #E910C6;
    text-decoration: none;
}

</style>
          
          
<script>       
    export default {
        name: 'StatisticsList',
        props: ['filteredResults','errorMsg','noResults','personalResults']
    }
</script>