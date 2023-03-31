<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Create Course</h1>
      </div>
    </div>
    <section class="section">
       <div class="px-5 py-5 has-background-grey-lighter">
            <h2 class="subtitle">Meta Information</h2>
            <div class="field">
                <label>Title</label>
                <input type="text" class="input" v-model="form.title">
            </div>
            <div class="field">
                <label>Short Description</label>
                <textarea  class="textarea" v-model="form.short_description"></textarea>
            </div>
            <div class="field">
                <label>Long Description</label>
                <textarea  class="textarea" v-model="form.long_description"></textarea>
            </div>
            <div class="field">
                <div class="select is-multiple">
                    <select multiple size="10" v-model="form.categories">
                        <option 
                            v-for="category in categories" :key="category.id"
                            :value="category.id"
                        >   {{ category.title }}
                        </option>
                    </select>
                </div>
            </div>
            <div class="mt-6 px-5 py-5 has-background-grey-lighter">
                <h2 class="subtitle">Lessons</h2>
                
                
                <div v-for="(lesson, index) in form.lessons" 
                    v-bind:key="index" 
                    class="mb-4">

                    <h3 class="subtitle is-size-6">lesson</h3>
                    <div class="field">
                        <label>Title</label>
                        <input type="text" class="input" v-model="lesson.title" :name="`form.lessons[${index}][title]`">
                    </div>
                    <div class="field">
                        <label>Short Description</label>
                        <textarea  class="textarea" v-model="lesson.short_description" :name="`form.lessons[${index}][short_description]`"></textarea>
                    </div>
                    <div class="field">
                        <label>Long Description</label>
                        <textarea  class="textarea" v-model="lesson.long_description" :name="`form.lessons[${index}][long_description]`"></textarea>
                    </div>
                    <hr>
                </div>

                <button class="button is-primary" @click="addLession()">Add lesson</button>
            </div>
            <div class="field buttons">
                <button class="button is-success" @click="submitForm('draft')">Save as Draft</button>
                <button class="button is-success" @click="submitForm('in_review')">Submit for review</button>
            </div>
        </div>
        
    </section>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    data() {
        return {
            form:{
                title: '',
                short_description: '',
                long_description:'',
                categories:[],
                status:'',
                lessons:[],
            },
            categories : [],
        }
    
    },
    mounted() {
        this.getCategories()
    },
    methods: {
        getCategories() {
            console.log('getcategories')
            axios
                .get('/courses/categories/')
                .then(response =>{
                    console.log(response.data)

                    this.categories = response.data
                })

       
        },
        submitForm(status) {
            console.log('submit form')
            console.log(this.form)

            this.form.status= status

            axios.post('courses/create-course/', this.form)
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error:', error)
                })
        },
        addLession() {
            console.log('Add Lession')
            this.form.lessons.push({
                title:'',
                short_description:'',
                long_description:'',
            })
        }
    }
}
</script>
