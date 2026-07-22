import React from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {unenroll} from '../store/enrollmentSlice';

export default function ProfilePage(){
  const enrolledCourses=useSelector(state=>state.enrollment.enrolledCourses);
  const dispatch=useDispatch();

  return (
    <div className='profile-card'>
      <h2>Student Profile & Enrolled Courses</h2>
      <p><strong>Name:</strong> Alex Johnson</p>
      <p><strong>Email:</strong> alex.j@university.edu</p>

      <h3 style={{marginTop:'2rem'}}>Enrolled Courses ({enrolledCourses.length})</h3>
      {enrolledCourses.length===0 ? (
        <p style={{marginTop:'0.5rem', color:'#64748b'}}>No courses enrolled yet.</p>
      ) : (
        <div className='enrolled-list'>
          {enrolledCourses.map(course=>(
            <div key={course.id} className='enrolled-item'>
              <div>
                <strong>{course.name}</strong> ({course.code}) - {course.credits} Credits
              </div>
              <button 
                type='button' 
                className='action-btn remove-btn' 
                onClick={()=>dispatch(unenroll(course.id))}
              >
                Un-enroll
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}