import React, {useState} from 'react';
import CourseCard from '../components/CourseCard';
import {initialCourses} from '../data/coursesData';

export default function CoursesPage(){
  const [searchTerm, setSearchTerm]=useState('');

  const filteredCourses=initialCourses.filter(course=>
    course.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    course.code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <input 
        type='text' 
        className='search-bar' 
        placeholder='Search courses by name or code...' 
        value={searchTerm}
        onChange={e=>setSearchTerm(e.target.value)}
      />
      <div className='course-grid'>
        {filteredCourses.map(course=>(
          <CourseCard key={course.id} {...course} />
        ))}
      </div>
    </div>
  );
}