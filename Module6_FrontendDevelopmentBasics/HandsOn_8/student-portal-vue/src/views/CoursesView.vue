<template>
  <div>
    <input 
      type='text' 
      class='search-bar' 
      placeholder='Search courses by name or code...' 
      v-model='searchTerm'
    />
    <div class='course-grid'>
      <CourseCard 
        v-for='course in filteredCourses' 
        :key='course.id' 
        v-bind='course' 
      />
    </div>
  </div>
</template>

<script setup>
import {ref, computed, onMounted} from 'vue';
import CourseCard from '@/components/CourseCard.vue';
import {initialCourses} from '@/data/coursesData';

const courses=ref([]);
const searchTerm=ref('');

onMounted(()=>{
  courses.value=initialCourses;
});

const filteredCourses=computed(()=>{
  return courses.value.filter(course=>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
    course.code.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});
</script>