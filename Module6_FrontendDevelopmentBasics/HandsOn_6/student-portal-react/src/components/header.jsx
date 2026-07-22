import React from 'react';
import {Link} from 'react-router-dom';
import {useSelector} from 'react-redux';

export default function Header(props){
  const enrolledCourses=useSelector(state=>state.enrollment.enrolledCourses);

  return (
    <header>
      <h1>
        <Link to='/'>{props.siteName}</Link>
      </h1>
      <nav>
        <ul>
          <li><Link to='/'>Home</Link></li>
          <li><Link to='/courses'>Courses</Link></li>
          <li><Link to='/profile'>Profile</Link></li>
          <li>
            <span className='enrolled-badge'>
              Enrolled: {enrolledCourses.length}
            </span>
          </li>
        </ul>
      </nav>
    </header>
  );
}