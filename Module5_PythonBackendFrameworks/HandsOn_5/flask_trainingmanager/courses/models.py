from app import db

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(100), unique=True, nullable=False)
    hod_name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False, default=0.0)

    skill_modules = db.relationship('SkillModule', back_populates='department', cascade="all, delete-orphan")
    employees = db.relationship('Employee', back_populates='department', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "dept_name": self.dept_name,
            "hod_name": self.hod_name,
            "budget": self.budget
        }

class SkillModule(db.Model):
    __tablename__ = 'skill_modules'
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(150), nullable=False)
    module_code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    department = db.relationship('Department', back_populates='skill_modules')
    certifications = db.relationship('Certification', back_populates='skill_module', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "module_name": self.module_name,
            "module_code": self.module_code,
            "credits": self.credits,
            "department_id": self.department_id
        }

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hiring_year = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    department = db.relationship('Department', back_populates='employees')
    certifications = db.relationship('Certification', back_populates='employee', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "hiring_year": self.hiring_year,
            "department_id": self.department_id
        }

class Certification(db.Model):
    __tablename__ = 'certifications'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(5), nullable=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    skill_module_id = db.Column(db.Integer, db.ForeignKey('skill_modules.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint('employee_id', 'skill_module_id', name='_employee_module_uc'),)

    employee = db.relationship('Employee', back_populates='certifications')
    skill_module = db.relationship('SkillModule', back_populates='certifications')

    def to_dict(self):
        return {
            "id": self.id,
            "grade": self.grade,
            "employee_id": self.employee_id,
            "skill_module_id": self.skill_module_id
        }