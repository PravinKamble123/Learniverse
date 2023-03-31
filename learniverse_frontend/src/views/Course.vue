<template>
    <div class="courses">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">{{ course.title }}</h1>
          <router-link :to="{name: 'Author', params: { id: course.created_by.id }}" class="subtitle">BY {{ course.created_by.first_name + ' ' + course.created_by.last_name }}</router-link>
        </div>
      </div>
      <section class="section">
        <div class="container">
            <div class="columns content">
                <div class="column is-2">
                    <h2>Table of content</h2>
                    <ul>
                        <li v-for="lesson in lessons" :key="lesson.id">
                            <a @click="setActivateLesson(lesson)">{{ lesson.title }}</a>
                        </li>
                    </ul>
                </div>

                <div class="column is-10">
                    
                    <template v-if="this.$store.state.user.isAuthenticated">
                        <template v-if="activeLesson">
                            <h2>{{ activeLesson.title }}</h2>

                            <span class="tag is-warning" v-if="activity.status == 'started'" @click="markAsDone">Started: mark this as done
                            </span>
                            <span class="tag is-success" v-else>Done</span>
                            <hr>
                            {{ activeLesson.long_description }}
                            <hr>

                            <template v-if="activeLesson.lesson_type === 'quiz'">
                                <Quiz
                                    v-bind:quiz="quiz"
                                    />
                            </template>
                            <template v-if="activeLesson.lesson_type === 'video'">
                                <AddVideo
                                    v-bind:youtube_id="activeLesson.youtube_id"
                                    />
                            </template>
                            <template v-if="activeLesson.lesson_type === 'article'">
                                <CourseComment 
                                    v-for="comment in comments" :key="comment.id"
                                    v-bind:comment="comment"
                                    />
                                <!-- AddComment component added     -->
                                <AddComment
                                    v-bind:course="course"
                                    v-bind:activeLesson="activeLesson"
                                    v-on:submitComment="submitComment"
                                />
                            </template>
                            
                        </template>

                        <template v-else>
                            {{ course.long_description }}
                        </template>
                            
                   
                    </template>
                    <template v-else>
                        <h2>Access Denied</h2>
                        <p>You need to have a account to continue!</p>
                    </template>
                </div>

            </div>
        </div>
    </section>
    </div>

</template>

<script>

import axios from "axios"
import CourseComment from '../components/CourseComment.vue'
import AddComment from '../components/AddComment.vue'
import Quiz from '../components/Quiz.vue'
import AddVideo from '../components/AddVideo.vue'




export default {
    components:{
    CourseComment,
    AddComment,
    Quiz,
    AddVideo,
},
    data() {
        return {
            course: {
                created_by:{
                    id:0
                }
            },
            lessons: [],
            comments:[],
            errors: [],
            quiz:{},
            activity: {},
            
            activeLesson: null,
            
            
        }
    },
   async mounted(){
        console.log('mounted')

        const slug = this.$route.params.slug;

       await axios
            .get(`/courses/${slug}`)
            .then(response => {
                console.log(response.data)

                this.course = response.data.course;
                this.lessons = response.data.lessons;
            })

        document.title = this.course.title + ' | Learniverse'
    },
    methods: {

        
        submitComment(comment){
            this.comments.push(comment)
        },
        setActivateLesson(lesson) {
            this.activeLesson=lesson
            
            // If lesson type is quiz we don't want to show the comment there
            if(lesson.lesson_type === 'quiz'){
                console.log('we are checking if lesson_type is quiz or not')
                this.getQuiz()
            }else {
                this.getComments()
            }

            this.tractStarted()
            
        },
        tractStarted() {
            axios.post(`/activities/track-started/${this.course.slug}/${this.activeLesson.slug}/`)
            .then(response => {
                console.log(response.data)

                this.activity = response.data
            })
        },
        markAsDone() {
            axios.post(`/activities/mark-as-done/${this.course.slug}/${this.activeLesson.slug}/`)
            .then(response => {
                console.log(response.data)

                this.activity = response.data
            })
        },
        getQuiz(){
            axios.get(`/courses/${this.course.slug}/${this.activeLesson.slug}/get-quiz/`)
            .then(response => {
                console.log('You are inside the quiz function')
                console.log(response.data)

                this.quiz=response.data
            })
        },
        getComments() {
            axios.get(`/courses/${this.course.slug}/${this.activeLesson.slug}/get-comments`)
            .then(response => {
                console.log(response.data)

                this.comments=response.data
            })
        },
        
    }
}
</script>

  