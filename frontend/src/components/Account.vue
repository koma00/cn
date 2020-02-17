<template>
  <div class="account">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Account',
  data () {
    return {
      msg: ''
    }
  },

  mounted () {
    axios
      .get('http://127.0.0.1:8000/api/v1/account/id3/')
      .then(response => (this.msg = response))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
