from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from typing import List, Optional
import time
from database import engine, Base, get_db
import models
import schemas
import security
from jose import jwt,JWTError



app = FastAPI(
    title="Course Management API",
    description="API to monitor employee skill development modules.",
    version="1.5.0",
    contact={
        "name": "Support Desk",
        "email": "company.support@corporate.in",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")


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

async def get_current_user(token: str=Depends(oauth2_scheme), db: AsyncSession=Depends(get_db)) -> models.User:
    try:
        payload=jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str=payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token properties.")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired or is invalid.")
        
    result=await db.execute(select(models.User).where(models.User.email == email))
    user=result.scalars().first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authenticated user no longer exists.")
    return user


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

@app.post('/api/v1/auth/register/', response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED, tags=['Authentication'])
async def register_user(user_in: schemas.UserRegister, db: AsyncSession=Depends(get_db)):
    existing_user_result=await db.execute(select(models.User).where(models.User.email == user_in.email))
    if existing_user_result.scalars().first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is already registered under an active account.")
        
    hashed_pwd=security.get_password_hash(user_in.password)
    new_user=models.User(email=user_in.email, hashed_password=hashed_pwd, is_active=True)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.post('/api/v1/auth/login/', response_model=schemas.Token, tags=['Authentication'])
async def login_user(form_data: OAuth2PasswordRequestForm=Depends(), db: AsyncSession=Depends(get_db)):
    result=await db.execute(select(models.User).where(models.User.email == form_data.username))
    user=result.scalars().first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email username or password confirmation.")
        
    access_token=security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post('/api/v1/courses/', response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, tags=['Courses'])
async def create_course(
    course: schemas.SkillModuleCreate, 
    response: Response, 
    db: AsyncSession=Depends(get_db),
    current_user: models.User=Depends(get_current_user)
):
    result=await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    if not result.scalars().first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Target department code mapping does not exist.")
        
    db_module=models.SkillModule(**course.model_dump())
    db.add(db_module)
    await db.commit()
    await db.refresh(db_module)
    response.headers['Location']=f'/api/v1/courses/{db_module.id}/'
    return db_module

@app.get('/api/v1/courses/', response_model=List[schemas.CourseResponse], tags=['Courses'])
async def get_courses(skip: int=0, limit: int=10, department_id: Optional[int]=None, db: AsyncSession=Depends(get_db)):
    query=select(models.SkillModule)
    if department_id is not None:
        query=query.where(models.SkillModule.department_id == department_id)
    query=query.offset(skip).limit(limit)
    result=await db.execute(query)
    return result.scalars().all()

@app.get('/api/v1/courses/{course_id}/', response_model=schemas.CourseResponse, tags=['Courses'])
async def get_course_detail(course_id: int, db: AsyncSession=Depends(get_db)):
    result=await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module=result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} does not exist")
    return db_module

@app.put('/api/v1/courses/{course_id}/', response_model=schemas.CourseResponse, tags=['Courses'])
async def update_course(course_id: int, course_data: schemas.SkillModuleUpdate, db: AsyncSession=Depends(get_db)):
    result=await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module=result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} does not exist")
        
    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(db_module, key, value)
        
    await db.commit()
    await db.refresh(db_module)
    return db_module

@app.delete('/api/v1/courses/{course_id}/', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(
    course_id: int, 
    db: AsyncSession=Depends(get_db),
    current_user: models.User=Depends(get_current_user)
):
    result=await db.execute(select(models.SkillModule).where(models.SkillModule.id == course_id))
    db_module=result.scalars().first()
    if not db_module:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} does not exist")
        
    await db.delete(db_module)
    await db.commit()
    return None