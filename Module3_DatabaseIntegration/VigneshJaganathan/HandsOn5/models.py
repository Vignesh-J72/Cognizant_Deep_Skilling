from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base 

user="root"
password="vigneshj722"
host="127.0.0.1"
port=3306
database="corporate_db"
base=declarative_base()

def create_connection():
    engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
    return engine

class department(base):
    __tablename__="departments"
    department_id=Column(Integer,primary_key=True,autoincrement=True)
    dept_name=Column(String(100),nullable=False,unique=True)
    hod_name=Column(String(100))
    budget=Column(Numeric(12,2))
    employees=relationship("Employee",back_populates="department")
    skill_modules=relationship("Skills",back_populates="department")
    instructors=relationship("Instructor",back_populates="department")

class employees(base):
    __tablename__="employees"
    employee_id=Column(Integer,primary_key=True,autoincrement=True)
    first_name=Column(String(50),nullable=False)
    last_name=Column(String(50),nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    date_of_birth=Column(Date)
    department_id=Column(Integer)
    hiring_year=Column(Integer)
    department=relationship("Department",back_populates="employees")
    certifications=relationship("Certifications",back_populates="employee",cascade="all,delete-orphan")

class Instructor(base):
    __tablename__ = 'instructors'
    instructor_id = Column(Integer, primary_key=True, autoincrement=True)
    instructor_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    salary = Column(Numeric(10, 2))
    department = relationship('Department', back_populates='instructors')

class Certification(base):
    __tablename__ = 'certifications'
    certification_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    module_id = Column(Integer, ForeignKey('skill_modules.module_id'))
    completion_date = Column(Date)
    grade = Column(String(2))
    employee = relationship('Employee', back_populates='certifications')
    skill_module = relationship('SkillModule', back_populates='certifications')

if __name__=="__main__":
    try:
        engine=create_connection()
        print(f"Connected to {database} successfully")
        base.metadata.create_all(engine)
    except Exception as e:
        print("An exception has occured:",e)
