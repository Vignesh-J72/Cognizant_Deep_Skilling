import React, {useState, useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import CourseCard from '../components/CourseCard';
import {
  fetchCoursesThunk, 
  selectCourses, 
  selectCoursesLoading, 
  selectCoursesError 
} from '../store/courseSlice';

export default function CoursesPage(){
  const dispatch=useDispatch();
  const courses=useSelector(selectCourses);
  const loading=useSelector(selectCoursesLoading);
  const error=useSelector(selectCoursesError);

  const [searchTerm, setSearchTerm]=useState('');

  useEffect(()=>{
    if(courses.length===0){
      dispatch(fetchCoursesThunk());
    }
  }, [dispatch, courses.length]);

  const filteredCourses=courses.filter(course=>
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

      {loading && <div className='loading-indicator'>Loading courses via Centralized API layer...</div>}
      {error && <div className='error-box'>Error: {error}</div>}

      {!loading && !error && (
        <div className='course-grid'>
          {filteredCourses.map(course=>(
            <CourseCard key={course.id} {...course} />
          ))}
        </div>
      )}
    </div>
  );
}