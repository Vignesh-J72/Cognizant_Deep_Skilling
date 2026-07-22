import React from 'react';
import {useParams, useNavigate} from 'react-router-dom';
import {useDispatch, useSelector} from 'react-redux';
import {initialCourses} from '../data/coursesData';
import {enroll} from '../store/enrollmentSlice';

export default function CourseDetailPage(){
  const {courseId}=useParams();
  const navigate=useNavigate();
  const dispatch=useDispatch();
  const enrolledCourses=useSelector(state=>state.enrollment.enrolledCourses);

  const course=initialCourses.find(c=>c.id===Number(courseId));
  
  if(!course){
    return <div className='detail-card'><h2>Course not found!</h2></div>;
  }

  const isEnrolled=enrolledCourses.some(c=>c.id===course.id);

  const handleEnroll=()=>{
    dispatch(enroll(course));
    navigate('/profile');
  };

  return (
    <div className='detail-card'>
      <h2>{course.name} ({course.code})</h2>
      <p><strong>Credits:</strong> {course.credits}</p>
      <p><strong>Grade Scheme:</strong> {course.grade}</p>
      <p style={{margin:'1rem 0'}}><strong>Description:</strong> {course.description}</p>
      <button 
        type='button' 
        className='action-btn' 
        onClick={handleEnroll}
        disabled={isEnrolled}
      >
        {isEnrolled ? 'Already Enrolled' : 'Enroll Now'}
      </button>
    </div>
  );
}