<template>
  <div class="account">
    {{ $route.params.id }}<br>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Account',
  props: ['id'],
  data () {
    return {
      msg: ''
    }
  },

  mounted () {
    if (!this.id) {
      this.acc_id = 0
    } else {
      this.acc_id = this.id
    }
    axios
      .get('http://127.0.0.1:8000/api/v1/account/id' + this.acc_id + '/')
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
