<template>
    <div class="statistics-list">
        <h4 id="top_left"> 100% </h4>
        <h4 id="bottom_left"> 1 </h4>
        
        <h4 id="bottom_right"> {{daysInMonth}} </h4>

        <h4 v-if="errorMsg">{{errorMsg }}</h4>
        
        <div class="graph_block">
        <div v-for="number in daysInMonth" v-bind:key="number" class="block" >

    <template v-for="result in filteredResults" v-bind:key="result.date">
     <div v-if="result.date && new Date(result.date).getDate() === number" 
     :style="{ 'height': result.percentage + '%' , 'opacity': ((Number(result.percentage)+10)/100 )}" 
     class="one_block">        
     </div>

    </template>
        
        </div>
        


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
    .statistics-list h4{
        margin: 0px;
        color: black;
    }

    #top_left{
        top: -1.1rem;
    left: -1.1rem;
    position: relative;
    }

    #bottom_left{
        bottom: -16rem;
    left: -1.1rem;
    position: relative;
    }

    #bottom_right{bottom: -15rem;
    right: -29rem;
    position: relative;
    }


    .graph_block{    
    background: #F1F2F1;
    padding: 5px;
    display: flex;
    width: 99%;
    height: 100%;
    justify-content: space-around;
    align-items: flex-end;
    top: -1.5rem;
    position: relative;
    border: 1px solid black;
   } 

   .block{
    width: 100%;
    height: 100%;
    margin: 0px 0.7px 0px 0.7px;
    display: flex;
    align-items: flex-end;}

.one_block{
    background-color: #00897B;   
    width: 100%;

}
    
    </style>
              
              
    <script>
        export default {
            name: 'StastisticsGraph',
            props: ['filteredResults','errorMsg', 'daysInMonth'],
           }
        
    </script>