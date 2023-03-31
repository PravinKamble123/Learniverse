<template>
  <Nav/>
  <router-view/>
  <Footer/>
</template>

<script>
import axios from 'axios'
import Nav from './components/Nav.vue'
import Footer from './components/Footer.vue'
export default {
  name:'App',
  components: {
    Nav,
    Footer
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.user.token
    
    if(token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token 
    }else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>

<style lang="scss">
@import '~bulma/bulma';

</style>
