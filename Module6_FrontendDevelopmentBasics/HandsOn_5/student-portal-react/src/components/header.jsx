import React from 'react';

export default function Header(props){
  return (
    <header>
      <h1>{props.siteName}</h1>
      <nav>
        <ul>
          <li><a href='#courses'>Courses</a></li>
          <li><a href='#profile'>Profile</a></li>
          <li>
            <span class='enrolled-badge'>
              Enrolled: {props.enrolledCount}
            </span>
          </li>
        </ul>
      </nav>
    </header>
  );
}