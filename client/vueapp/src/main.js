import { createApp } from 'vue'
import App from './App.vue'
import {router} from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'
import unoverlay from 'unoverlay-vue'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: "AIzaSyApvP_rAWmeX1VsrVf0woeBLlD6ogIO6js",
  authDomain: "codeinthedark-edf6f.firebaseapp.com",
  projectId: "codeinthedark-edf6f",
  storageBucket: "codeinthedark-edf6f.appspot.com",
  messagingSenderId: "264167012462",
  appId: "1:264167012462:web:908f25f6a5beecaaaa8e7f",
  measurementId: "G-DB1X0KH43N"
};

initializeApp(firebaseConfig);

const app = createApp(App)
app.use(router)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(unoverlay)  
app.component('font-awesome-icon', FontAwesomeIcon)
library.add(fas)
app.mount('#app')