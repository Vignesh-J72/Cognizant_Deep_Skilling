<template>
  <div class='profile-card'>
    <h2>Student Profile & Enrolled Courses</h2>
    <p><strong>Name:</strong> Alex Johnson</p>
    <p><strong>Email:</strong> alex.j@university.edu</p>

    <h3 style='margin-top:2rem;'>
      Enrolled Courses ({{ enrollmentStore.enrolledCourses.length }}) — Total Credits: {{ enrollmentStore.totalCredits }}
    </h3>

    <p v-if='enrollmentStore.enrolledCourses.length === 0' style='margin-top:0.5rem; color:#64748b;'>
      No courses enrolled yet.
    </p>

    <div v-else class='enrolled-list'>
      <div 
        v-for='course in enrollmentStore.enrolledCourses' 
        :key='course.id' 
        class='enrolled-item'
      >
        <div>
          <strong>{{ course.name }}</strong> ({{ course.code }}) - {{ course.credits }} Credits
        </div>
        <button 
          type='button' 
          class='action-btn remove-btn' 
          @click='enrollmentStore.unenroll(course.id)'
        >
          Un-enroll
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import {useEnrollmentStore} from '@/stores/enrollment';

const enrollmentStore=useEnrollmentStore();
</script>