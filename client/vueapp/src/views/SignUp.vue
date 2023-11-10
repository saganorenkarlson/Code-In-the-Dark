<template>
<div class="sign_up" >
<the-card>  
    <template  v-slot:left>
        <div class="input-wrapper">
        <span class="icon"><font-awesome-icon icon="fa-solid fa-envelope" /></span>
        <input class="text_input" type="text" placeholder="E-mail"  v-model="email"/> 
        </div>
 
        <div class="input-wrapper">
        <span class="icon"><font-awesome-icon icon="fa-solid fa-lock" /></span>
        <input class="text_input" type="password" placeholder="Password" v-model="password"/> 
        </div>
        <p v-if="errMsg">{{ errMsg }}  </p>


<my-button label="Begin" @click="register"> </my-button>
 <button-overall @click="register" label="Sign up" >  </button-overall> 

 <p id="or"> or </p>

 <div class="input-wrapper">
        <span class="icon" id="google">
            <img class="img_icon" :src="iconSrc" alt="My Icon">
        </span>
        <google-btn @click="signInWithGoogle" label="Sign up with Google" > </google-btn>
        </div>

<div id="have_account">
<p> Already have an account? </p> <p id="underline" @click="toSignIn"> Sign in. </p>
</div>
</template>

<template  v-slot:right>

    <h1> Welcome</h1>
    <p> You thought you knew front-end..</p>

</template>

</the-card>
</div>
</template>
  
<script setup> 
import {ref} from "vue";
import {getAuth, createUserWithEmailAndPassword, GoogleAuthProvider,signInWithPopup} from "firebase/auth";
import { useRouter } from "vue-router";
import { useResultsStore } from "../stores/results.js";
const resultsStore = useResultsStore();

const email= ref("");
const password= ref("");
const router = useRouter();
const errMsg= ref();
const register = () => {
    console.log(password.value);
    createUserWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((data)=> {
        console.log("succesfully registerd");
        console.log(data);
        resultsStore.newUser().then(() => {
            router.push('/profile');
        });
    }).catch((error) => {
      switch (error.code){
                case "auth/email-already-in-use":
                errMsg.value="An account with that email already exists";
                break;
                default:
                errMsg.value="An error occured";
                break;
            }    });
}

const signInWithGoogle = () => {
    const provider = new GoogleAuthProvider();
  signInWithPopup(getAuth(), provider)
    .then((result) => {
      console.log(result.user);
      resultsStore.newUser().then(() => {
        router.push('/profile');
      });    })
    .catch((error) => {
      switch (error.code){
                case "auth/email-already-in-use":
                errMsg.value="An account with that email already exists";
                break;
                default:
                errMsg.value="An error occured";
                break;
            }
    });
};


const toSignIn = () =>{
    router.push("/sign-in");
}

</script>

<script>
import CardSignUp from "../components/cards/CardSignUpIn.vue";

import ButtonOverall from "../components/buttons/ButtonOverall.vue";
    import GoogleButton from "../components/buttons/GoogleButton.vue";


export default {
name: 'HomePage',
  components: {
    'the-card': CardSignUp,
    'button-overall': ButtonOverall,
        'google-btn': GoogleButton
  },
      data(){
        return{iconSrc: require('@/assets/logoG.png'),}
      }
  }
</script>

<style>
.sign_up{
    width:100vw;
    height:100vh;
    display: flex;
    align-content: center;
    justify-content: center;
    align-items: center;
    flex-direction: column;

}
.icon .svg-inline--fa  {
  height: 2rem;
}

#underline{
    margin-left: 5px;
    text-decoration: underline;
}
#have_account{
    display: flex;
}

</style>