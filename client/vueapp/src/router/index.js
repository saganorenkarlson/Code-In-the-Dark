import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'
//import TemplatePage from '../views/TemplatePage.vue'
import {getAuth, onAuthStateChanged} from "firebase/auth"

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/game',
    name: 'game',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/GamePage.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/profile',
    name: 'profile',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/ProfilePage.vue'),
    meta: {
      requiresAuth: true,
    },
  }, 
  {
    path: '/sign-in',
    name: 'sign-in',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: SignIn,
    
    meta:{
      cantBeLoggedIn: true,
    }
  }, 
  {
    path: '/sign-up',
    name: 'sign-up',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: SignUp,
    meta:{
      cantBeLoggedIn: true,
    }
    
  },
  {
    path: '/template',
    name: 'template',
    component: () => import(/* webpackChunkName: "about" */ '../views/TemplatePage.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/statistics',
    name: 'statistics',
    component: () => import(/* webpackChunkName: "about" */ '../views/StatisticsPage.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/friends',
    name: 'friends',
    component: () => import('../views/FriendsPage.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/friends/:username',
    name: 'friend',
    component: () => import('../views/FriendProfile.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    // Catch-all route for all other paths
    path: '/:catchAll(.*)',
    component: HomePage,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


const getCurrentUser = () => {
  return new Promise((resolve, reject) =>{
    
    const removeListner = onAuthStateChanged(
      getAuth(),(user)=>{
        console.log(user)
        removeListner();
        resolve(user);
      }, 
      reject
    );
  });
}

router.beforeEach(async(to,from,next) => {
if(to.matched.some((record) => record.meta.requiresAuth)){
if(await getCurrentUser()){
next();
}
else{
  alert("you dont have access!");
  next("/");
}

}
else if (to.matched.some((record) => record.meta.cantBeLoggedIn)) {
  //console.log(getAuth().currentUser)
  if (await getCurrentUser()) {
    // Prevent navigation to "sign-up" or "sign-in" if user is already logged in
    next("/profile");
  } else {
    next();
  }
} else {
  next();
}

}

);

export{router, getCurrentUser}

