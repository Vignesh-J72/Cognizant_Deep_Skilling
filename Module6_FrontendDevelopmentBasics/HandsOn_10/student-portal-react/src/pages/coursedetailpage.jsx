import React, {useState, useEffect} from 'react';
import {useParams, useNavigate} from 'react-router-dom';
import {useDispatch, useSelector} from 'react-redux';
import {getCourseById} from '../api/courseApi';
import {enrollCourseThunk, selectEnrolledCourses} from '../store/courseSlice';

export default function CourseDetailPage(){
  const {courseId}=useParams();
  const navigate=useNavigate();
  const dispatch=useDispatch();
  const enrolledCourses=useSelector(selectEnrolledCourses);

  const [course, setCourse]=useState(null);
  const [loading, setLoading]=useState(true);

  useEffect(()=>{
    getCourseById(courseId)
      .then(data=>{
        setCourse(data);
        setLoading(false);
      })
      .catch(()=>{
        setLoading(false);
      });
  }, [courseId]);

  if(loading){
    return <div className='loading-indicator'>Loading course detail from API...</div>;
  }

  if(!course){
    return <div className='detail-card'><h2>Course not found!</h2></div>;
  }

  const isEnrolled=enrolledCourses.some(c=>c.id===course.id);

  const handleEnroll=async()=>{
    await dispatch(enrollCourseThunk({studentId:1, course})).unwrap();
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