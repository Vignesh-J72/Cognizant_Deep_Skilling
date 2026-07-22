<template>
  <div class='detail-card' v-if='course'>
    <h2>{{ course.name }} ({{ course.code }})</h2>
    <p><strong>Credits:</strong> {{ course.credits }}</p>
    <p><strong>Grade Scheme:</strong> {{ course.grade }}</p>
    <p style='margin:1rem 0;'><strong>Description:</strong> {{ course.description }}</p>
    <button 
      type='button' 
      class='action-btn' 
      @click='handleEnroll'
      :disabled='isEnrolled'
    >
      {{ isEnrolled ? 'Already Enrolled' : 'Enroll Now' }}
    </button>
  </div>
  <div class='detail-card' v-else>
    <h2>Course not found!</h2>
  </div>
</template>

<script setup>
import {computed} from 'vue';
import {useRoute, useRouter} from 'vue-router';
import {useEnrollmentStore} from '@/stores/enrollment';
import {initialCourses} from '@/data/coursesData';

const route=useRoute();
const router=useRouter();
const enrollmentStore=useEnrollmentStore();

const course=computed(()=>{
  return initialCourses.find(c=>c.id===Number(route.params.id));
});

const isEnrolled=computed(()=>{
  return course.value && enrollmentStore.enrolledCourses.some(c=>c.id===course.value.id);
});

function handleEnroll(){
  if(course.value){
    enrollmentStore.enroll(course.value);
    router.push('/profile');
  }
}
</script>