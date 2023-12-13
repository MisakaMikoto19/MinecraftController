
from flask import request
from flask_restful import Resource
from .minecraft_server import runservice

class TestReturn(Resource):
    def get(self):
        return {'message': 'test return message'}
    
class TestReturn2(Resource):
    def get(self):
        return {'message': 'test return 2 message!!!!!!!!!!!!'}
    
class StartServer(Resource):
    def post(self):
        params = request.get_json()
        data = runservice.RunService(params)
        return {
            "code": 10000,
            "message": "succeed",
            "data": data
        }
    
