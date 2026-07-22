from flask import Blueprint, jsonify, request
from app import db
from .models import SkillModule,Employee, Certification

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')


def make_response_json(data, status_code=200, status_text="success"):
    return jsonify({'status': status_text, 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def get_courses():
    modules = SkillModule.query.all()
    return make_response_json([m.to_dict() for m in modules], 200)

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json() or {}
    required = ['module_name', 'module_code', 'credits', 'department_id']
    missing = [f for f in required if f not in data]
    if missing:
        return make_response_json({"error": f"Missing attributes: {', '.join(missing)}"}, 400, "fail")
        
    new_module = SkillModule(
        module_name=data['module_name'],
        module_code=data['module_code'],
        credits=data['credits'],
        department_id=data['department_id']
    )
    db.session.add(new_module)
    db.session.commit()
    return make_response_json(new_module.to_dict(), 201)

@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course_detail(course_id):
    module = SkillModule.query.get_or_404(course_id)
    return make_response_json(module.to_dict(), 200)

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    module = SkillModule.query.get_or_404(course_id)
    data = request.get_json() or {}
    
    module.module_name = data.get('module_name', module.module_name)
    module.module_code = data.get('module_code', module.module_code)
    module.credits = data.get('credits', module.credits)
    module.department_id = data.get('department_id', module.department_id)
    
    db.session.commit()
    return make_response_json(module.to_dict(), 200)

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    module = SkillModule.query.get_or_404(course_id)
    db.session.delete(module)
    db.session.commit()
    return make_response_json({"message": f"Module {course_id} completely removed."}, 200)

@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    SkillModule.query.get_or_404(course_id)
    
    enrolled_employees = db.session.query(Employee).\
        join(Certification, Employee.id == Certification.employee_id).\
        filter(Certification.skill_module_id == course_id).all()
        
    return make_response_json([emp.to_dict() for emp in enrolled_employees], 200)