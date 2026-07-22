from flask import Flask, jsonify
from config import Config
from courses.routes import courses_bp

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({
            "status": "error",
            "data": {"error": "The requested URL or resource path was not found on this API framework server."}
        }), 404

    @app.errorhandler(500)
    def handle_server_error(error):
        return jsonify({
            "status": "error",
            "data": {"error": "An internal system server error occurred."}
        }), 500

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)