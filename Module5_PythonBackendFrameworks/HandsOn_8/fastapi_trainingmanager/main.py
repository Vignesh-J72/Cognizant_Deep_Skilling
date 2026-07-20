from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from typing import List, Optional
import time

from database import engine, Base, get_db
import models
import schemas

app = FastAPI(
    title="Course Management API",
    description="API to monitor employee skill development modules.",
    version="1.5.0",
    contact={
        "name": "Support Desk",
        "email": "company.support@corporate.in",
    }
)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """
    Standardizes manual HTTPException occurrences into the required error template.
    """
    # Dynamically derive clear error code strings based on HTTP status
    code_map = {
        400: "BAD_REQUEST",
        401: "UNAUTHORIZED",
        403: "FORBIDDEN",
        404: "NOT_FOUND",
        422: "UNPROCESSABLE_ENTITY"
    }
    error_code = code_map.get(exc.status_code, "SERVER_ERROR")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": error_code,
                "message": exc.detail,
                "field": None
            }
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Catches built-in schema validation syntax errors and reformats them.
    """
    errors = exc.errors()
    first_error = errors[0] if errors else {}
    
    # Trace field mapping hierarchy location (e.g., body -> credits)
    field_path = " -> ".join([str(p) for p in first_error.get("loc", []) if p != "body"])
    message = first_error.get("msg", "Schema validation error occurred.")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": "UNPROCESSABLE_ENTITY",
                "message": f"Validation failed: {message}",
                "field": field_path if field_path else None
            }
        }
    )


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

@app.get('/', include_in_schema=False)
def read_root():
    return {'message': 'API running'}


#background task
def send_confirmation_email(student_email: str):
    time.sleep(1) 
    print(f"Sending confirmation to {student_email}")



@app.post(
    '/api/courses/', 
    response_model=schemas.CourseResponse, 
    status_code=status.HTTP_201_CREATED,
    tags=['Courses'],
    summary="Create a new course module",
    response_description="Returns the structural database entity details of the newly created skill module."
)
async def create_course(
    course: schemas.SkillModuleCreate, 
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    if not result.scalars().first():
        raise HTTPException(status_code=400, detail="Target department code mapping does not exist.")
        
    db_module = models.SkillModule(**course.model_dump())
    db.add(db_module)
    await db.commit()
    await db.refresh(db_module)
    
    background_tasks.add_task(send_confirmation_email, "employee@corporate.in")
    
    return db_module

@app.get(
    '/api/courses/', 
    response_model=List[schemas.CourseResponse], 
    tags=['Courses'], 
    summary="List all available courses"
)
async def get_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    query = select(models.SkillModule)
    if department_id is not None:
        query = query.where(models.SkillModule.department_id == department_id)
        
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@app.get(
    '/api/courses/{course_id}/', 
    response_model=schemas.CourseResponse, 
    tags=['Courses'], 
    summary="Fetch target course profile details"
)
async def get_course_detail(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module = result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_module

@app.put(
    '/api/courses/{course_id}/', 
    response_model=schemas.CourseResponse, 
    tags=['Courses'], 
    summary="Modify properties of an existing course"
)
async def update_course(course_id: int, course_data: schemas.SkillModuleUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module = result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=404, detail="Course not found")
        
    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(db_module, key, value)
        
    await db.commit()
    await db.refresh(db_module)
    return db_module

@app.delete(
    '/api/courses/{course_id}/', 
    status_code=status.HTTP_204_NO_CONTENT, 
    tags=['Courses'], 
    summary="Remove a course record permanently"
)
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module = result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=404, detail="Course not found")
        
    await db.delete(db_module)
    await db.commit()
    return None