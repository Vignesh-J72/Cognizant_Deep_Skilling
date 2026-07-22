import {courses} from './data.js';

let currentCourses=[];

const fetchUserThen=id=>{
    fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(res=>res.json())
        .then(user=>console.log('Fetch Then User Name:', user.name));
};

const fetchUserAsync=async id=>{
    try{
        const res=await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        const user=await res.json();
        console.log('Async/Await User Name:', user.name);
    }catch(err){
        console.error('Fetch User Error:', err);
    }
};

fetchUserThen(1);
fetchUserAsync(1);

const fetchAllCourses=()=>{
    return new Promise(resolve=>{
        setTimeout(()=>resolve(courses), 1000);
    });
};

const loadMultipleUsers=async()=>{
    try{
        const [u1, u2]=await Promise.all([
            fetch(`https://jsonplaceholder.typicode.com/users/1`).then(r=>r.json()),
            fetch(`https://jsonplaceholder.typicode.com/users/2`).then(r=>r.json())
        ]);
        console.log('Promise.all Users:', u1.name, '|', u2.name);
    }catch(err){
        console.error('Promise.all Error:', err);
    }
};

loadMultipleUsers();

axios.interceptors.request.use(config=>{
    console.log('API call started:', config.url);
    return config;
});

const apiFetch=async(url, options={})=>{
    const res=await fetch(url, options);
    if(!res.ok){
        throw new Error(`HTTP Error! Status: ${res.status}`);
    }
    return await res.json();
};

const gridContainer=document.querySelector('.course-grid');
const totalCreditsEl=document.getElementById('total-credits');
const searchInput=document.getElementById('search-courses');
const sortBtn=document.getElementById('sort-btn');
const selectedCourseEl=document.getElementById('selected-course');
const coursesLoadingEl=document.getElementById('courses-loading');

const notifLoadingEl=document.getElementById('notif-loading');
const notifErrorEl=document.getElementById('notif-error');
const notifGridEl=document.querySelector('.notif-grid');
const retryBtn=document.getElementById('retry-btn');

const calculateTotalCredits=items=>items.reduce((sum, course)=>sum+course.credits, 0);

const renderGrid=items=>{
    gridContainer.innerHTML='';
    const fragment=document.createDocumentFragment();
    items.forEach(course=>{
        const {id, name, code, credits, grade}=course;
        const article=document.createElement('article');
        article.className='course-card';
        article.dataset.id=id;
        article.innerHTML=`
            <div>
                <h3>${name}</h3>
                <div class='course-code'>${code}</div>
                <p>Enrolled course module in academic curriculum.</p>
            </div>
            <div class='course-footer'>
                <span class='course-credits'>Credits: ${credits}</span>
                <span class='course-grade'>Grade: ${grade}</span>
            </div>
        `;
        fragment.appendChild(article);
    });
    gridContainer.appendChild(fragment);
    totalCreditsEl.textContent=`Total Enrolled Credits: ${calculateTotalCredits(items)}`;
};

const initCourses=async()=>{
    coursesLoadingEl.style.display='block';
    const loadedCourses=await fetchAllCourses();
    currentCourses=[...loadedCourses];
    coursesLoadingEl.style.display='none';
    renderGrid(currentCourses);
};

initCourses();

const renderNotifications=posts=>{
    notifGridEl.innerHTML='';
    const fragment=document.createDocumentFragment();
    posts.forEach(post=>{
        const article=document.createElement('article');
        article.className='notif-card';
        article.innerHTML=`
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;
        fragment.appendChild(article);
    });
    notifGridEl.appendChild(fragment);
};

const loadNotificationsAxios=async(shouldFail=false)=>{
    notifLoadingEl.style.display='block';
    notifErrorEl.style.display='none';
    retryBtn.style.display='none';
    notifGridEl.innerHTML='';

    const targetUrl=shouldFail 
        ? 'https://jsonplaceholder.typicode.com/nonexistent' 
        : 'https://jsonplaceholder.typicode.com/posts';

    try{
        const response=await axios.get(targetUrl, {params:{userId:1}});
        renderNotifications(response.data);
    }catch(err){
        notifErrorEl.textContent=`Failed to load notifications: ${err.message}`;
        notifErrorEl.style.display='block';
        retryBtn.style.display='inline-block';
    }finally{
        notifLoadingEl.style.display='none';
    }
};

loadNotificationsAxios(true);

retryBtn.addEventListener('click', ()=>loadNotificationsAxios(false));

searchInput.addEventListener('input', e=>{
    const query=e.target.value.toLowerCase();
    const filtered=currentCourses.filter(course=>course.name.toLowerCase().includes(query));
    renderGrid(filtered);
});

sortBtn.addEventListener('click', ()=>{
    currentCourses.sort((a, b)=>b.credits-a.credits);
    renderGrid(currentCourses);
});

gridContainer.addEventListener('click', e=>{
    const card=e.target.closest('.course-card');
    if(!card) return;
    const courseId=Number(card.dataset.id);
    const selected=currentCourses.find(c=>c.id===courseId);
    if(selected){
        const {name, grade}=selected;
        selectedCourseEl.textContent=`Selected Course: ${name} | Current Grade: ${grade}`;
    }
});