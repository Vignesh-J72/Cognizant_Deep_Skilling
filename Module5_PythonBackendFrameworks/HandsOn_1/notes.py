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




"""
