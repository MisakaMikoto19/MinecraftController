from flask_restful import Resource

class TestReturn(Resource):
    def get(self):
        return {'message': 'test return message'}
    
class TestReturn2(Resource):
    def get(self):
        return {'message': 'test return 2 message!!!!!!!!!!!!'}