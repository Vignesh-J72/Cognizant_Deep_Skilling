import React, {useState} from 'react';

export default function StudentProfile(){
  const [profile, setProfile]=useState({
    name:'Alex Johnson',
    email:'alex.j@university.edu',
    semester:'6'
  });

  const handleChange=(e)=>{
    const {name, value}=e.target;
    setProfile(prev=>({
      ...prev,
      [name]:value
    }));
  };

  return (
    <div class='profile-card'>
      <h2>Student Profile</h2>
      <form class='profile-form' onSubmit={e=>e.preventDefault()}>
        <div class='form-group'>
          <label htmlFor='name'>Full Name</label>
          <input 
            type='text' 
            id='name' 
            name='name' 
            value={profile.name} 
            onChange={handleChange} 
          />
        </div>
        <div class='form-group'>
          <label htmlFor='email'>Email Address</label>
          <input 
            type='email' 
            id='email' 
            name='email' 
            value={profile.email} 
            onChange={handleChange} 
          />
        </div>
        <div class='form-group'>
          <label htmlFor='semester'>Current Semester</label>
          <input 
            type='number' 
            id='semester' 
            name='semester' 
            value={profile.semester} 
            onChange={handleChange} 
          />
        </div>
      </form>
    </div>
  );
}