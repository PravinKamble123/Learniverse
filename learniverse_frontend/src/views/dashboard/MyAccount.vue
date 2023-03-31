<template>
    <div class="about">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">My Account</h1>
        </div>
      </div>
      <section class="section">
        <div class="columns is-multiline">
          <div class="column is-12">
            <h2 class="subtitle is-size-3">Your active courses</h2>
          </div>
          <div class="column is-4"

          v-for="course in courses" :key="course.id"
          >
            <CourseItem :course="course" />
          </div>
        </div>
        <hr>
        <button @click="logout()" class="button is-danger">Log out</button>
      </section>
    </div>
  </template>

<script>
import CourseItem from '@/components/CourseItem.vue'
import axios from 'axios'
export default {
    components: {
      CourseItem
    },
    data() {
      return {
        courses: []
      }
    },
    mounted() {
      axios.get('/activities/active-courses/')
        .then(response => {
          console.log(response.data)

          this.courses=response.data
        })
    },
    methods: {
        logout() {
            console.log('Log out!')
            
            axios.defaults.headers.common['Authorization'] = ""
            localStorage.removeItem('token')

            this.$store.commit('removeToken')
            this.$router.push('/')
        }
    }
}

</script>
  