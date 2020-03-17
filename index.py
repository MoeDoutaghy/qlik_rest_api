import flask
from flask import request, jsonify, make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Predefined messages to start with.
messages = [
    {
        'id': 0,
        'message': 'Dinner is ready',
        'palindrome': 'False'
    },
    {
        'id': 1,
        'message': 'Did you get your lunch',
        'palindrome': 'False'
    },
    {
        'id': 2,
        'message': 'Was it a car or a cat I saw?',
        'palindrome': 'True'
    }
]


# This function is used to determine whether the message is palindrome or not.
# Special characters and spaces are removed from the string before doing string comparision.
def is_palindrome(message):
    string = (''.join(e for e in message if e.isalnum())).lower()
    if string == string[::-1]:
        return True
    return False


@app.errorhandler(409)
def resource_conflict(error):
    return make_response(jsonify({'error': 'Resource already exists'}), 409)


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Resource not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Parameters are missing'}), 400)


@app.route('/v1/mma/messages/all', methods=['GET'])
def get_all():
    return jsonify(messages)


@app.route('/v1/mma/messages', methods=['GET'])
def get_message():
    if 'id' in request.args:
        msg_id = int(request.args['id'])
    else:
        return bad_request(400)
    for message in messages:
        if message['id'] == msg_id:
            return jsonify(message)
    return page_not_found(404)


@app.route('/v1/mma/messages', methods=['POST'])
def create_message():
    if 'message' not in request.get_json():
        return bad_request(400)
    message = {
        'id': messages[-1]['id'] + 1,
        'message': request.get_json().get('message'),
        'palindrome': is_palindrome(request.get_json().get('message'))
    }
    messages.append(message)
    return jsonify({'message': message}), 201


@app.route('/v1/mma/messages', methods=['DELETE'])
def delete_message():
    if 'id' in request.get_json():
        msg_id = int(request.get_json().get('id'))
    else:
        return bad_request(400)
    for message in messages:
        if message['id'] == msg_id:
            messages.remove(message)
            return jsonify({'Delete': 'Done'})
    return page_not_found(404)


@app.route('/v1/mma/messages', methods=['PUT'])
def update_message():
    if 'id' in request.get_json() and 'message' in request.get_json():
        msg_id = int(request.get_json().get('id'))
    else:
        return bad_request(400)
    for message in messages:
        if message['id'] == msg_id:
            # message['id'] = msg_id
            message['message'] = request.get_json().get('message')
            message['palindrome'] = is_palindrome(request.get_json().get('message'))
    return jsonify({'message': message}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
