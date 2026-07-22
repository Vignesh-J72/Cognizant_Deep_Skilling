import React, {useState, useEffect} from 'react';
import Header from './components/Header';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import {initialCourses} from './data/coursesData';

export default function App(){
  const [courses, setCourses]=useState([]);
  const [enrolledCourses, setEnrolledCourses]=useState([]);
  const [searchTerm, setSearchTerm]=useState('');
  const [loading, setLoading]=useState(true);
  const [error, setError]=useState(null);

  useEffect(()=>{
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res=>{
        if(!res.ok){
          throw new Error('Failed to fetch remote courses data');
        }
        return res.json();
      })
      .then(()=>{
        setCourses(initialCourses);
        setLoading(false);
      })
      .catch(err=>{
        setError(err.message);
        setCourses(initialCourses);
        setLoading(false);
      });
  }, []);

  useEffect(()=>{
    console.log('Courses state updated:', courses);
  }, [courses]);

  const handleEnroll=(course)=>{
    if(!enrolledCourses.some(c=>c.id===course.id)){
      setEnrolledCourses(prev=>[...prev, course]);
    }
  };

  const filteredCourses=courses.filter(course=>
    course.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    course.code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className='app-container'>
      <Header siteName='Student Portal' enrolledCount={enrolledCourses.length} />
      <main>
        <input 
          type='text' 
          className='search-bar' 
          placeholder='Search courses by name or code...' 
          value={searchTerm}
          onChange={e=>setSearchTerm(e.target.value)}
        />

        {loading && <div className='loading-text'>Loading courses...</div>}
        {error && <div className='error-box'>Note: {error}. Loaded offline fallback courses.</div>}

        <div className='course-grid'>
          {filteredCourses.map(course=>(
            <CourseCard 
              key={course.id} 
              {...course} 
              onEnroll={handleEnroll}
              isEnrolled={enrolledCourses.some(c=>c.id===course.id)}
            />
          ))}
        </div>

        <StudentProfile />
      </main>
    </div>
  );
}