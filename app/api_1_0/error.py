def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response

@api.errorhandler(ValidarionError)
def validarionerror(e):
    return bad_request(e.args[0])