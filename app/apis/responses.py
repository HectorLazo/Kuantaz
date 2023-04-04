from flask import jsonify

def bad_request(message= 'Bad request'):
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': message,
            'code': 400
        }
    ), 400

def not_found(message='Resource not found'):
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': message,
            'code': 404
        }
    ), 404

def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200