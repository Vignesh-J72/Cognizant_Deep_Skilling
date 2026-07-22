from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class UserRegister(BaseModel):
    email: EmailStr
    password: str=Field(..., min_length=8)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token: str
    token_type: str

class SkillModuleBase(BaseModel):
    module_name: str=Field(..., max_length=150)
    module_code: str=Field(..., max_length=20)
    credits: int=Field(..., ge=1)
    department_id: int

class SkillModuleCreate(SkillModuleBase):
    pass

class SkillModuleUpdate(BaseModel):
    module_name: Optional[str]=None
    module_code: Optional[str]=None
    credits: Optional[int]=None
    department_id: Optional[int]=None

class CourseResponse(SkillModuleBase):
    id: int

    class Config:
        from_attributes=True