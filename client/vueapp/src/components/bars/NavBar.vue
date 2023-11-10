<template>
    <div class="nav-bar">
        <h1 class="nav-bar-text">code in the DARK</h1>
        <DropDownMenu/>
    </div>
</template>

<style>
.nav-bar {
    background-color: black;
    display: flex;
    height: 6rem;
    flex-direction: row;
    align-content: stretch;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    top: 0;
    width: 100%;
}

.nav-bar-text {
    margin-left: 1rem;
    color: #00897B;
    font-size: 3.5rem;
}

</style>
  
  
<script>  
import DropDownMenu from "../DropDownMenu.vue";

export default {
    name: 'NavBar',
    components: {
    'DropDownMenu': DropDownMenu,
}
}

</script>