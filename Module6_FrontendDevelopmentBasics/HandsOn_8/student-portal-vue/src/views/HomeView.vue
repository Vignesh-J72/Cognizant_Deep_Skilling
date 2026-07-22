<template>
  <div class='hero-box'>
    <h2>Welcome to the Student Portal</h2>
    <p>Browse available modules, inspect course details, and manage your academic enrollment.</p>
    <RouterLink to='/courses' class='primary-btn'>Explore Courses</RouterLink>
  </div>
</template>

<script setup>
import {RouterLink} from 'vue-router';
</script>