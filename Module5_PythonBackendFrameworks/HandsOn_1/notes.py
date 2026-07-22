#Task 1

#1. API
"""
Middleware:
The GET /api/courses/ request arrives to the middleware first. Each layer of the middleware passes 
it to next layer. These layers check the request or modify it like perofrming security actions,etc.

URL routing:
After the request passes through the middleware layers, it reaches the url router. The urls.py file 
contains necessary urls defined in the project. The incoming request is matched with the avilable urls in
urls.py and returns the first matching url. It determines which class should handle it.

View:
The request is sent to the associated view. The view processes the request.

Model:
The model is contacted by the view. The model performs a database search and return the values from database.
The model executes query on MongoDB.

View:
The view handles the result set and packages it into an HTTP response back.

Middleware:
The http object passes though the middleware layers in reverse again.
it is returned as http response.

"""
#2
"""
The middleware processes the incoming request, modifying it before sending it to the view.
After the response is generated , the middleware again modifies the response when it passes through the layers.

I. Security (django.middleware.security.SecurityMiddleware):
    It performs security functions by enforcing HTTPS connections and setting browser headers.

II. Session (django.contrib.sessions.middleware.SessionMiddleware):
    It is responsible for session support. Sessions are used to store user information across
    different requests like authentication, etc.

"""

#3
"""
WSGI: Web Server Gateway Interface
    It is designed for web application and used in synchronous communication manner as traditional request-response way.
    WSGI supports http only and does not have websocket support. It is synchronous and affects performance in 
    asynchronous applications.

ASGI: Asynchronous Web Server Interface
    It is designed for asynchronous applications. It can handle multiple requests concurrently without
    blocking other requests. It efficiently handles requests for long sessions or many clients.
    
By default, Django uses WSGI. ASGI is used only when the application needs to handle multiple users asynchronously.

"""
#4
"""
MVC-
M- Model. It interacts with the database passes the query results to the controller.
V- View. It displays the results to the user and pushes user input to controller.
C- Controller. It handles the interaction between Model and View.

Django MVT -
M- Model. It is unchanged from the MVC achitecture.
V- View. View performs the duties of the controller in MVT instead.
T- Template. It does the work of View in MVC architecture.

"""
