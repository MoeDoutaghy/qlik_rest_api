import flask
from flask import request, jsonify, abort, make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
        id = int(request.args['id'])
    else:
        return bad_request(400)
    for message in messages:
        if message['id'] == id:
            messages.append(message)
            return jsonify(message)
    return page_not_found(404)


@app.route('/v1/mma/messages', methods=['POST'])
def create_message():
    if 'message' not in request.args:
        return bad_request(400)
    else:
        message = {
            'id': messages[-1]['id'] + 1,
            'message': request.args['message'],
            'palindrome': request.args['palindrome']
        }
        messages.append(message)
        return jsonify({'message': message}), 201


@app.route('/v1/mma/messages', methods=['DELETE'])
def delete_message():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return bad_request(400)
    for message in messages:
        if message['id'] == id:
            messages.remove(message)
            return jsonify({'Delete': 'Done'})
    return page_not_found(404)


@app.route('/v1/mma/messages', methods=['PUT'])
def update_message():
    id_found = False
    if 'id' in request.args and 'message' in request.args and 'palindrome' in request.args:
        id = int(request.args['id'])
    else:
        return bad_request(400)
    for message in messages:
        if message['id'] == id:
            message['id'] = id
            message['message'] = request.args['message']
            message['palindrome'] = request.args['palindrome']
    return jsonify({'message': message})


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')