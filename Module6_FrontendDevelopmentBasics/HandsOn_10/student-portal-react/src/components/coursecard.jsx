import React from 'react';
import {Link, useNavigate} from 'react-router-dom';
import {useDispatch, useSelector} from 'react-redux';
import {enrollCourseThunk, selectEnrolledCourses} from '../store/courseSlice';

export default function CourseCard(course){
  const {id, name, code, credits, description}=course;
  const dispatch=useDispatch();
  const navigate=useNavigate();
  const enrolledCourses=useSelector(selectEnrolledCourses);
  
  const isEnrolled=enrolledCourses.some(c=>c.id===id);

  const handleEnroll=async()=>{
    await dispatch(enrollCourseThunk({studentId:1, course})).unwrap();
    navigate('/profile');
  };

  return (
    <div className='course-card'>
      <div>
        <h3>
          <Link to={`/courses/${id}`}>{name}</Link>
        </h3>
        <div className='course-code'>{code}</div>
        <p>{description}</p>
      </div>
      <div className='course-footer'>
        <span className='course-credits'>Credits: {credits}</span>
        <button 
          type='button' 
          className='action-btn' 
          onClick={handleEnroll}
          disabled={isEnrolled}
        >
          {isEnrolled ? 'Enrolled' : 'Enroll'}
        </button>
      </div>
    </div>
  );
}