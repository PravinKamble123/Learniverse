<template>
    <nav class="navbar is-info" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <a class="navbar-item is-size-4" href="/">Learniverse</a>
    
        </div>

        <div id="navbar-item" class="navbar-menu">
            <div class="navbar-start">
                <a href="/" class="navbar-item">Home</a>
                <a href="/about" class="navbar-item">About</a>
                <router-link to="/courses" class="navbar-item">Courses</router-link>
            </div>
        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <template v-if="this.$store.state.user.isAuthenticated">
                        <router-link to="/dashboard/create-course" class="button is-primary">Create Course</router-link>
                        <router-link to="/dashboard/my-account" class="button is-info">My Account</router-link>
                    </template>
                    <template v-else>
                        <a href="/signup" class="button is-primary"><strong>Sign Up</strong></a>
                        <a href="/log-in" class="button is-light"><strong>Log in</strong></a>
                    </template>
                    
                </div>
            </div>
        </div>
        </div>
  </nav>
</template>