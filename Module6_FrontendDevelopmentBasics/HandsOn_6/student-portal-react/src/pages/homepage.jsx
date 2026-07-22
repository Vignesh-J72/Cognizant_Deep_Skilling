import React from 'react';
import {Link} from 'react-router-dom';

export default function HomePage(){
  return (
    <div className='hero-box'>
      <h2>Welcome to the Student Portal</h2>
      <p>Browse available modules, inspect course details, and manage your academic enrollment.</p>
      <Link to='/courses' className='primary-btn'>Explore Courses</Link>
    </div>
  );
}