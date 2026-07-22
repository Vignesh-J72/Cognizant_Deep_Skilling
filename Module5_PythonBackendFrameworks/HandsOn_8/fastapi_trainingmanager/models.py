from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    dept_name = Column(String(100), unique=True, nullable=False)
    hod_name = Column(String(100), nullable=False)
    budget = Column(Float, default=0.0)
    skill_modules = relationship("SkillModule", back_populates="department")

class SkillModule(Base):
    __tablename__ = 'skill_modules'
    id = Column(Integer, primary_key=True, index=True)
    module_name = Column(String(150), nullable=False)
    module_code = Column(String(20), unique=True, nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    department = relationship("Department", back_populates="skill_modules")