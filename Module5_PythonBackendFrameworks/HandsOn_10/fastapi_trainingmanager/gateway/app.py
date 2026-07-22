from flask import Flask, request, Response
import requests

app=Flask(__name__)

SERVICES={
    "courses": "http://localhost:5001",
    "students": "http://localhost:5002"
}

@app.route('/api/<string:service>/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/<string:service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway_proxy(service, path):
    if service not in SERVICES:
        return {"error": "Target service route not found"}, 404
    base_target=SERVICES[service]
    target_url=f"{base_target}/api/{service}/{path}"
    if request.query_string:
        target_url+=f"?{request.query_string.decode('utf-8')}"
    try:
        response=requests.request(
            method=request.method,
            url=target_url,
            headers={k: v for k, v in request.headers if k.lower()!='host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=5
        )
        return Response(response.content, response.status_code, response.headers.items())
    except requests.exceptions.ConnectionError:
        return {"error": f"Backend service '{service}' is unreachable"}, 503

if __name__=='__main__':
    app.run(port=5000, debug=True)