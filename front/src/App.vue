<template>
  <div id="app">
    <h1>Hello {{name}}</h1>
    <h2>visits: {{visits}}</h2>
  </div>
</template>

<script>
import Axios from 'axios';

export default {
  name: 'App',
  data () {
		return {
      name: null,
      visits: null
		};
	},

  mounted() {
    Axios.get("http://localhost:5000/api").then((response) => {
      this.name = response.data.name
      this.visits = response.data.visits
		}).catch((error) => {
			alert(error);
		});
	},

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
