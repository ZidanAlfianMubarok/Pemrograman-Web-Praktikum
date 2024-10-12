from flask_restful import Resource

def initialize_routes(api):
    api.add_resource(HelloWorld, '/')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}