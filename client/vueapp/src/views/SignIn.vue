<template>

<div class="sign_in" >
<the-card>  
    <template  v-slot:left>
       
        <div class="input-wrapper">
        <span class="icon"><font-awesome-icon icon="fa-solid fa-envelope" /></span>
        <input class="text_input" type="text" placeholder="E-mail"  v-model="email"/> 
        </div>
 
        <div class="input-wrapper">
        <span class="icon" ><font-awesome-icon icon="fa-solid fa-lock" /></span>
        <input class="text_input" type="password" placeholder="Password" v-model="password"/> 
        </div>

 
 <p v-if="errMsg">{{ errMsg }}  </p>

 
 <button-overall @click="register" label="Sign in" >  </button-overall> 
<p id="or"> or </p>
    <div class="input-wrapper">
        <span class="icon" id="google">
            <img class="img_icon" :src="iconSrc" alt="My Icon">
        </span>
        <google-btn @click="signUpWithGoogle" label="Sign in with Google" > </google-btn>
        </div>


<div id="have_account">
<p>Don't have an account? </p> <p id="underline" @click="toSignUp">Create.</p>
</div>
</template>

<template  v-slot:right>

    <h1> Welcome</h1>
    <p> Next challenge in:</p>
    <count-down> </count-down>

</template>

</the-card>
</div>

        
    </template>
      
    
    <script setup> 
    import {ref} from "vue";
    import {getAuth, signInWithEmailAndPassword,GoogleAuthProvider,signInWithPopup} from "firebase/auth";
    import { useRouter } from "vue-router";
    import { useResultsStore } from "../stores/results.js";
    const resultsStore = useResultsStore();


    const email= ref("");
    const password= ref("");
    const errMsg= ref();
    const router = useRouter();
    const register = () => {
        signInWithEmailAndPassword(getAuth(), email.value, password.value)
        .then((data)=> {
            console.log("succesfully registerd");
            console.log(data.user.uid);
            resultsStore.fetchResults().then(() => {
                router.push('/profile');
            });        
          }).catch((error) => {
            console.log(error.code);
            switch (error.code){
                case "auth/invalid-email":
                errMsg.value="Invalid email";
                break;
                case "auth/user-not-found":
                errMsg.value="No account with that email was found";
                break;
                case "auth/wrong-password":
                errMsg.value="Incorrect password";
                break;
                default:
                errMsg.value="Email or password was incorrect";
                break;
            }
        });
    }

    const signUpWithGoogle = () => {
 const provider = new GoogleAuthProvider();
 signInWithPopup(getAuth(), provider)
 .then((result)=> {
  
  console.log("a ba");
    resultsStore.fetchResults().then(() => {
      router.push('/profile');
    }); 
  }).catch((error)=>{
    
    console.log("a error");
    console.log(error.code);
 })
};


    const toSignUp = () =>{
    router.push("/sign-up");
}
    
    </script>
    
    <script>
    import CardSignUp from "../components/cards/CardSignUpIn.vue";
    import CountDown from "../components/countDowns/CountDown.vue";
    import ButtonOverall from "../components/buttons/ButtonOverall.vue";

    import GoogleButton from "../components/buttons/GoogleButton.vue";

    export default {
    name: 'HomePage',
      components: {
        'the-card': CardSignUp,
        'count-down': CountDown,
        'button-overall': ButtonOverall,
        'google-btn': GoogleButton
      },
      data(){
        return{iconSrc: require('@/assets/logoG.png'),}
      }
      }
    </script>
    
    <style>
.icon {
  position: absolute;
  left: 17%; /* Adjust the value as needed to position the icon */
  top: 50%;
  transform: translateY(-50%);
  size: 10px;
  color: #969696;
  /* Add any additional styling for your icon, such as size, color, etc. */
}

.icon .svg-inline--fa  {
  height: 2rem;
}

#google{
    left: 23%;
}

.input-wrapper {
  position: relative;
  width: 100%;
  display: flex;
    justify-content: center;
}
.sign_in{
    width:100vw;
    height:100vh;
    display: flex;
    align-content: center;
    justify-content: center;
    align-items: center;
    flex-direction: column;

}

#or{
    margin: 20px 0px 0px 0px;
}

.text_input{
  height: 2.4rem;
  width: 60%;
  background-color: #D9D9D9;
  box-shadow: 0px 0px 26px 2px #00897B;
border-radius: 8px;
color: #6a6a6a;
font-family: 'Cascadia Code', sans-serif;
font-size: 1.2rem;
border: 0px;
margin: 10px 0px 10px 0px;
padding-left: 3.1rem;
}

.text_input::placeholder{
  color: #969696;
}

.img_icon{
    height: 1.8rem;
}

.svg-inline--fa{
    height: 2rem
}
</style>