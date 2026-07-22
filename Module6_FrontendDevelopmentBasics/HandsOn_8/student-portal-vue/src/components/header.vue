<template>
  <header>
    <h1>
      <RouterLink to='/'>Student Portal</RouterLink>
    </h1>
    <nav>
      <ul>
        <li><RouterLink to='/'>Home</RouterLink></li>
        <li><RouterLink to='/courses'>Courses</RouterLink></li>
        <li><RouterLink to='/profile'>Profile</RouterLink></li>
        <li>
          <span class='enrolled-badge'>
            Enrolled: {{ enrollmentStore.enrolledCourses.length }}
          </span>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
import {RouterLink} from 'vue-router';
import {useEnrollmentStore} from '@/stores/enrollment';

const enrollmentStore=useEnrollmentStore();
</script>