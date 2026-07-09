from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

MOCK_DB = [
    {"id": 1, "module_name": "Python Backend", "module_code": "CS101", "credits": 4}
]

def make_response_json(data, status_code=200, status_text="success"):
    return jsonify({
        'status': status_text,
        'data': data
    }), status_code

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return make_response_json(MOCK_DB, 200)

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    
    if not data:
        return make_response_json({"error": "Content-Type must be application/json"}, 400, "fail")
        
    required_fields = ['module_name', 'module_code', 'credits']
    missing = [field for field in required_fields if field not in data]
    if missing:
        return make_response_json({"error": f"Missing required fields: {', '.join(missing)}"}, 400, "fail")
        
    new_module = {
        "id": len(MOCK_DB) + 1,
        "module_name": data['module_name'],
        "module_code": data['module_code'],
        "credits": data['credits']
    }
    MOCK_DB.append(new_module)
    return make_response_json(new_module, 201)

@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course_detail(course_id):
    module = next((item for item in MOCK_DB if item["id"] == course_id), None)
    if not module:
        return make_response_json({"error": "Resource not found"}, 404, "fail")
    return make_response_json(module, 200)

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    module = next((item for item in MOCK_DB if item["id"] == course_id), None)
    if not module:
        return make_response_json({"error": "Resource not found"}, 404, "fail")
        
    data = request.get_json() or {}
    module["module_name"] = data.get("module_name", module["module_name"])
    module["module_code"] = data.get("module_code", module["module_code"])
    module["credits"] = data.get("credits", module["credits"])
    
    return make_response_json(module, 200)

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    global MOCK_DB
    module = next((item for item in MOCK_DB if item["id"] == course_id), None)
    if not module:
        return make_response_json({"error": "Resource not found"}, 404, "fail")
        
    MOCK_DB = [item for item in MOCK_DB if item["id"] != course_id]
    return make_response_json({"message": f"Module {course_id} successfully deleted"}, 200)