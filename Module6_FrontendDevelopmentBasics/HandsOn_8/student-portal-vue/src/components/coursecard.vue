<template>
  <div class='course-card'>
    <div>
      <h3>
        <RouterLink :to='`/courses/${id}`'>{{ name }}</RouterLink>
      </h3>
      <div class='course-code'>{{ code }}</div>
      <p>{{ description }}</p>
    </div>
    <div class='course-footer'>
      <span class='course-credits'>Credits: {{ credits }}</span>
      <button 
        type='button' 
        class='action-btn' 
        @click='handleEnroll'
        :disabled='isEnrolled'
      >
        {{ isEnrolled ? 'Enrolled' : 'Enroll' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import {computed} from 'vue';
import {RouterLink, useRouter} from 'vue-router';
import {useEnrollmentStore} from '@/stores/enrollment';

const props=defineProps({
  id:Number,
  name:String,
  code:String,
  credits:Number,
  grade:String,
  description:String
});

const router=useRouter();
const enrollmentStore=useEnrollmentStore();

const isEnrolled=computed(()=>{
  return enrollmentStore.enrolledCourses.some(c=>c.id===props.id);
});

function handleEnroll(){
  enrollmentStore.enroll({
    id:props.id,
    name:props.name,
    code:props.code,
    credits:props.credits,
    description:props.description
  });
  router.push('/profile');
}
</script>