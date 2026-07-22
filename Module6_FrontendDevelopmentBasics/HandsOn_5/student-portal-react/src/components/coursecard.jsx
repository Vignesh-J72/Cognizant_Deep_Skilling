import React from 'react';

export default function CourseCard({id, name, code, credits, grade, onEnroll, isEnrolled}){
  return (
    <div class='course-card'>
      <div>
        <h3>{name}</h3>
        <div class='course-code'>{code}</div>
        <p>Enrolled course module in academic curriculum.</p>
      </div>
      <div class='course-footer'>
        <span class='course-credits'>Credits: {credits}</span>
        <button 
          type='button' 
          class='enroll-btn' 
          onClick={()=>onEnroll({id, name, code, credits})}
          disabled={isEnrolled}
        >
          {isEnrolled ? 'Enrolled' : 'Enroll'}
        </button>
      </div>
    </div>
  );
}