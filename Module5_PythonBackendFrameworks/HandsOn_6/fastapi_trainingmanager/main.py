from fastapi import FastAPI, Depends, HTTPException, status, Request, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from typing import List, Optional
from database import engine, Base, get_db
import models
import schemas

app = FastAPI(title='Course Management API', version='1.0')

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        async with async_sessionmaker(engine, class_=AsyncSession)() as session:
            check_dept = await session.execute(select(models.Department))
            if not check_dept.scalars().first():
                d1 = models.Department(dept_name="Computer Science", hod_name="Dr. Alan Turing", budget=500000.0)
                session.add(d1)
                await session.commit()

@app.get('/')
def read_root():
    return {'message': 'API running'}

@app.post('/api/courses/', response_model=schemas.SkillModuleResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: schemas.SkillModuleCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    if not result.scalars().first():
        raise HTTPException(status_code=400, detail="Target department code mapping does not exist.")
        
    db_module = models.SkillModule(**course.model_dump())
    db.session.add(db_module) if hasattr(db, 'session') else db.add(db_module)
    await db.commit()
    await db.refresh(db_module)
    return db_module

@app.get('/api/courses/', response_model=List[schemas.SkillModuleResponse])
async def get_courses(
    skip: int = 0, 
    limit: int = 10, 
    department_id: Optional[int] = None, 
    db: AsyncSession = Depends(get_db)
):
    query = select(models.SkillModule)
    if department_id is not None:
        query = query.where(models.SkillModule.department_id == department_id)
        
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@app.get('/api/courses/{course_id}/', response_model=schemas.SkillModuleResponse)
async def get_course_detail(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module = result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=404, detail="Skill Module resource missing.")
    return db_module

@app.put('/api/courses/{course_id}/', response_model=schemas.SkillModuleResponse)
async def update_course(course_id: int, course_data: schemas.SkillModuleUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module = result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=404, detail="Skill Module resource missing.")
        
    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(db_module, key, value)
        
    await db.commit()
    await db.refresh(db_module)
    return db_module

@app.delete('/api/courses/{course_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module = result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=404, detail="Skill Module resource missing.")
        
    await db.delete(db_module)
    await db.commit()
    return None