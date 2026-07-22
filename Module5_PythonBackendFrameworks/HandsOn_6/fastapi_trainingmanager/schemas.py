from pydantic import BaseModel, Field
from typing import Optional, List

class SkillModuleBase(BaseModel):
    module_name: str=Field(..., max_length=150)
    module_code: str=Field(..., max_length=20)
    credits: int=Field(..., ge=1)
    department_id:int

class SkillModuleCreate(SkillModuleBase):
    pass

class SkillModuleUpdate(BaseModel):
    module_name:Optional[str]=None
    module_code:Optional[str]=None
    credits: Optional[int]=None
    department_id: Optional[int]=None

class SkillModuleResponse(SkillModuleBase):
    id:int

    class Config:
        from_attributes=True

class DepartmentResponse(BaseModel):
    id: int
    dept_name: str
    hod_name: str
    budget: float
    skill_modules: List[SkillModuleResponse] = []  # Nested relation arrays

    class Config:
        from_attributes = True