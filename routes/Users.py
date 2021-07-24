from logs.logs import log_message
from flask import request, jsonify
from flask_restful import Resource

from werkzeug.exceptions import *
from helpers.validation import *
from logs import *

class Users(Resource):
  def post(self):
    try:
      data = request.get_json()

      username = data['username']
      password = data['password']
      
      if is_password_correct(username, password):
        return jsonify({'message': f'{username} has been succesfully registered'})
      else:
        raise BadRequest('The password is incorrect')
    except Exception as exc:
      log_message(exc)
      raise exc