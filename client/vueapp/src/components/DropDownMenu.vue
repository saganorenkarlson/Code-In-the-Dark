<template>
<nav @mouseenter="active = true" @mouseleave="active = false">
<div :class="['drop-down-menu-wrapper', {'drop-down-menu-wrapper-active': active}]" >
<font-awesome-icon class="nav-bar-icon" icon="fa-solid fa-user"/>
<div class="drop-down-menu-options" v-if="active" >
    <router-link class="drop-down-menu-option" to="/profile">
        <span v-on:click="active = false">Profile</span>
        </router-link>
    <router-link class="drop-down-menu-option" to="/statistics">
        <span v-on:click="active = false">Statistics</span>
    </router-link> 
    <router-link class="drop-down-menu-option" to="/friends">
        <span v-on:click="active = false">Friends</span>
    </router-link> 
    <router-link class="drop-down-menu-option" to="/sign-in"> 
        <span v-on:click="logOut">Log out</span>
        <font-awesome-icon class="drop-down-icon" icon="fa-solid fa-right-from-bracket"/>
    </router-link>
</div>
</div>
</nav>
</template>

<style>
.nav-bar-icon {
    font-size: 3rem;
    color: #00897B;
    margin: 1rem 1rem 1rem 1rem;
}

.drop-down-icon {
    padding-left: 0.5rem;
}

.drop-down-menu-wrapper {
    display: flex;
    position:relative;
    border-radius: 1rem;
    width: 5rem;
    justify-content: center;
}

.drop-down-menu-wrapper .svg-inline--fa{
    height: 3rem;
}


.drop-down-menu-option .svg-inline--fa{
    height: 1rem;
}

.drop-down-menu-wrapper:hover {
    background-color: #363636;
    cursor: pointer;
}

.drop-down-menu-wrapper-active{
    background-color: #363636;
}

.drop-down-menu-options {
    position:absolute;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    background-color: rgba(150,150,150,1);
    width: 10rem;
    height: 7rem;
    right: 0;
    top: 5.3rem;
    border-radius: 1rem;
    overflow: hidden;

}

.drop-down-menu-option {
    height: 100%;
    display: flex;
    align-items: center;
    color: white;
    text-decoration: none;
    font-weight: 300;
    padding-left: 0.7rem;
}


.drop-down-menu-option:hover {
    background-color: rgb(171, 171, 171);
}
</style>
  
  
<script>  
import { getAuth } from "firebase/auth";
import { useResultsStore } from "@/stores/results";

export default {
    name: 'DropDownMenu',
    data() {
    return { active: false } },
    methods:{
    logOut(){
        const auth = getAuth();
        auth.signOut()
        const store = useResultsStore();
        store.reset();
        //Work around to actually remove the state from localStorage
        setTimeout(() => {
            localStorage.removeItem('results');
        }, "1000");

    },},
}
</script>