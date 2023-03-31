<template>
    <div class="signup">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Sign UP</h1>
        </div>
      </div>
      <section class="section">
        <div class="container">
            <div class="column">
                <div class="column is-4 is-offset-4">
                    <form v-on:submit.prevent="submitForm">
                        <div class="field">
                            <label>Email</label>
                            <div class="control">
                                <input type="email" class="input" v-model="username">

                            </div>
                        </div>
                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input type="Password" class="input" v-model="password">
                                
                            </div>
                        </div>
                        <div class="field">
                            <label>Repeat Password</label>
                            <div class="control">
                                <input type="Password" class="input" v-model="password2">
                                
                            </div>
                        </div>
                        <div class="notification is-danger" v-if="errors.length">
                            <p
                            v-for="error in errors"
                            v-bind:key="error"
                            >
                            {{ error }}
                                
                            </p>
                        </div>

                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">Sign Up</button>
                            </div>
                        </div>
                    </form>

                    
                    <hr>
                    Or <router-link to="/log-in">click here</router-link> to Log in!
                </div>
            </div>
        </div>
      </section>
    </div>
  </template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm(){
            console.log('Submit Form')
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing!')
            }

            if (this.password === '') {
                this.errors.push('The password is missing!')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords are not matching...!')
            }

            if(!this.errors.length) {
                const formData = {
                    username : this.username,
                    password: this.password
                }

               axios
                    .post('/users/', formData)
                    .then(response => {
                        this.$router.push('/log-in')
                    }) 
                    .catch(error =>{
                        if (error.response) {
                            for( const property in error.response.data) {
                                this.error.push(`${property}:${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        }else if(error.message) {
                            this.error.push("Something went wrong. Please try again")

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>
  