<template>
    <div class="search_div">
      <input type="text"  class="search_user" v-model="searchQuery" @input="handleInput" />
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: ''
      };
    },
    methods: {
      handleInput() {
        // Call the handleSearch function with the current search query
        this.handleSearch(this.searchQuery);
      }
    },
    props: {
      handleSearch: {
        type: Function,
        required: true
      }
    }
  };
  </script>
  
  <style>
.search_user{
    height: 30px;
    width: 80%;
background: #D9D9D9;
box-shadow: 0px 0px 26px 2px #00897B;
border-radius: 10px;
border:None;
font-family: 'Cascadia Code', sans-serif;
    font-size: 1.2rem;
}

.search_div{
    width: 100%;
    margin-top: 10px;
    margin-bottom: 20px;
    display: flex;
}

input {
text-indent: 5px;
}

</style>