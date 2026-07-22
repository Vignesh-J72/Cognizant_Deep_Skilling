import React from 'react';
import {Link, useNavigate} from 'react-router-dom';
import {useDispatch, useSelector} from 'react-redux';
import {enroll} from '../store/enrollmentSlice';

export default function CourseCard({id, name, code, credits, description}){
  const dispatch=useDispatch();
  const navigate=useNavigate();
  const enrolledCourses=useSelector(state=>state.enrollment.enrolledCourses);
  
  const isEnrolled=enrolledCourses.some(c=>c.id===id);

  const handleEnroll=()=>{
    dispatch(enroll({id, name, code, credits, description}));
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