import {courses} from './data.js';

let currentCourses=[...courses];

const formattedCourses=currentCourses.map(course=>{
    const {name, code, credits}=course;
    return `${code} — ${name} (${credits} credits)`;
});
console.log('Formatted Courses:', formattedCourses);

const highCreditCourses=currentCourses.filter(course=>course.credits>=4);
console.log('High Credit Courses Count:', highCreditCourses.length);

const calculateTotalCredits=items=>items.reduce((sum, course)=>sum+course.credits, 0);
console.log('Total Enrolled Credits:', calculateTotalCredits(currentCourses));

const gridContainer=document.querySelector('.course-grid');
const totalCreditsEl=document.getElementById('total-credits');
const searchInput=document.getElementById('search-courses');
const sortBtn=document.getElementById('sort-btn');
const selectedCourseEl=document.getElementById('selected-course');

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

renderGrid(currentCourses);

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
    const selected=courses.find(c=>c.id===courseId);
    if(selected){
        const {name, grade}=selected;
        selectedCourseEl.textContent=`Selected Course: ${name} | Current Grade: ${grade}`;
    }
});