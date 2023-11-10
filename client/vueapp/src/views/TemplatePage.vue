<!-- Just a template page to see how the requests to the backend can be done-->

<template>
  <div>
    <h1>Data from API endpoint:</h1>
    <ul>
      <li v-for="result in results" :key="result.id">
        {{ result.date }} - {{ result.percentage }}%
      </li>
    </ul>
  </div>
</template>

<style>
li {
  color:white;
}
</style>

<script>
import axios from 'axios';
import { getAuth, onAuthStateChanged } from 'firebase/auth';

const auth = getAuth();

export default {
  name: 'TemplatePage',
  data() {
    return {
      results: [],
    };
  },
  async mounted() {
  await new Promise((resolve) => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        resolve();
      }
    });
  });

  const token = await this.accessToken();
  const name = await this.getName();
  const config = {
    headers: { Authorization: `Bearer ${token}` },
    params: {
    username: name
  }
  };

  axios
    .get('http://localhost:8000/api/user', config)
    .then((response) => {
      this.results = response.data.results;
    })
    .catch((error) => {
      console.error(error);
    });
},
  methods: {
    async accessToken() {
      const user = auth.currentUser;
      const token = await user.getIdToken();
      return token;
    },
    async getName() {
      const user = auth.currentUser;
      const name = user.email;
      return name;
    },
  },
};
</script>
