from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        """Return a hello world message."""
        return jsonify({'test': 'hello world'})

class NotFound(Resource):
    def get(self, resource):
        """
        Handle not found resource.
        ---
        parameters:
          - name: resource
            in: path
            type: string
            required: true
            description: The resource that was not found
        responses:
          404:
            description: Resource not found
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Resource not found"
        """
        return {'message': 'Resource not found'}, 404

def initialize_routes(api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(NotFound, '/<path:resource>')

if __name__ == '__main__':
    initialize_routes(api)
    app.run(debug=True)