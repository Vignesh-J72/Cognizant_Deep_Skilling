from datetime import date
from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, joinedload
from models import Department, Employee, SkillModule, Certification, Instructor,base


''' Performance of N+1 problem: It takes 9 queries to get the result without joinedload.
    Performance of eager loading: It only takes 1 single query to load through use of joinedload. '''

user="root"
password="vigneshj722"
host="127.0.0.1"
port=3306
database="corporate_db"
engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def add_people():
    dept_1=Department(dept_name="Computer Science",hod_name="Dr abdul",budget=Decimal("50000.00"))
    dept_2=Department(dept_name="Electrical Engineering", hod_name="Dr Mani", budget=Decimal("400000.00"))
    dept_3=Department(dept_name="Mechanical Engineering", hod_name="Dr Ram", budget=Decimal("350000.00"))
    session.add_all([dept_1,dept_2,dept_3])
    session.commit()
    e1 = Employee(first_name="Akash", last_name="Jagan", email="akash@gmail.com", date_of_birth=date(2000, 1, 1), department_id=dept_1.department_id, hiring_year=2024)
    e2 = Employee(first_name="Banu", last_name="Singh", email="banu@company.com", date_of_birth=date(1995, 5, 12), department_id=dept_1.department_id, hiring_year=2022)
    e3 = Employee(first_name="Chandar", last_name="Babu", email="chandar@company.com", date_of_birth=date(1998, 8, 20), department_id=dept_2.department_id, hiring_year=2024)
    e4 = Employee(first_name="Dee", last_name="Babu", email="dee@company.com", date_of_birth=date(1993, 11, 2), department_id=dept_3.department_id, hiring_year=2021)
    e5 = Employee(first_name="Ganesh", last_name="Kumar", email="ganesh@company.com", date_of_birth=date(1997, 3, 15), department_id=dept_1.department_id, hiring_year=2023)
    session.add_all([e1,e2,e3,e4,e5])
    session.commit()

    m1 = SkillModule(module_name="Introduction to NoSQL", module_code="CS101", credits=4, department_id=dept_1.department_id)
    m2 = SkillModule(module_name="Microservices Architecture", module_code="CS102", credits=4, department_id=dept_1.department_id)
    m3 = SkillModule(module_name="Circuit Analysis", module_code="EE201", credits=3, department_id=dept_2.department_id)
    session.add_all([m1,m2,m3])
    session.commit()

    c1 = Certification(employee_id=e1.employee_id, module_id=m1.module_id, completion_date=date.today(), grade="A")
    c2 = Certification(employee_id=e2.employee_id, module_id=m1.module_id, completion_date=date.today(), grade="B")
    c3 = Certification(employee_id=e1.employee_id, module_id=m2.module_id, completion_date=date.today(), grade="A")
    c4 = Certification(employee_id=e3.employee_id, module_id=m3.module_id, completion_date=date.today(), grade="C")
    session.add_all([c1, c2, c3, c4])
    session.commit()
    
    #deleting
    cert=session.query(Certification).filter(Certification.certification_id==c3.certification_id).first()
    if cert:
        session.delete(cert)
        session.commit()
        print(f"{c3.certification_id} deleted")

def read_record():
    computer=session.query(Employee).join(Department).filter(Department.dept_name=="Computer Science").all()
    print("N+1 loading")
    for i in computer:
        print(f"Name: {i.first_name} {i.last_name},Course: {i.certifications}")

    certs=session.query(Certification).all()
    print("Certifications")
    for i in certs:
        print(i)

def read_better():
    print("Eager loading")
    cert=session.query(Certification).options(joinedload(Certification.employee),joinedload(Certification.skill_module)).all()
    for i in cert:
        print(i)

def update_():
    emp=session.query(Employee).filter(Employee.email=="dee@company.com").first()
    emp.hiring_year=2026
    session.commit()

if __name__=="__main__":
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
    print("New run")
    add_people()
    read_record()
    read_better()
    update_()
    
    
    

    