import apiClient from './apiClient';

export const fallbackCourses=[
  {id:1, name:'Web Development Foundations', code:'CS101', credits:3, grade:'A', description:'Learn HTML5, CSS3, JavaScript, and Modern Front-End Frameworks.'},
  {id:2, name:'Data Structures & Algorithms', code:'CS102', credits:4, grade:'A-', description:'Master arrays, linked lists, trees, graphs, sorting, and dynamic programming.'},
  {id:3, name:'Database Management Systems', code:'CS201', credits:3, grade:'B+', description:'Relational model, ER modeling, normalization, and SQL query optimization.'},
  {id:4, name:'Software Engineering Principles', code:'CS301', credits:3, grade:'A', description:'Agile development, software design patterns, and unit testing frameworks.'},
  {id:5, name:'Computer Networks', code:'CS401', credits:4, grade:'B', description:'TCP/IP model, routing protocols, sockets programming, and network security.'}
];

export const getAllCourses=async()=>{
  const posts=await apiClient.get('/posts?_limit=5');
  return posts.map((post, idx)=>({
    id:fallbackCourses[idx]?.id || post.id,
    name:fallbackCourses[idx]?.name || post.title,
    code:fallbackCourses[idx]?.code || `CS10${post.id}`,
    credits:fallbackCourses[idx]?.credits || 3,
    grade:fallbackCourses[idx]?.grade || 'A',
    description:fallbackCourses[idx]?.description || post.body
  }));
};

export const getCourseById=async(id)=>{
  await apiClient.get(`/posts/${id}`);
  return fallbackCourses.find(c=>c.id===Number(id)) || fallbackCourses[0];
};

export const enrollStudent=async(studentId, courseId)=>{
  return await apiClient.post('/posts', {studentId, courseId});
};