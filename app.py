from flask import Flask
from flask_restful import Api

# import Routes
from routes.Users import Users

# Declare app
app = Flask(__name__)
api = Api(app)

# Add routes to app
api.add_resource(Users, '/users')

# Run app
if __name__ == 'main':
  app.run()