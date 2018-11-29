from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1': 'Tarek', '2': 'Freya'}
_IDS = {val: id for id, val in _USERS.items()}


class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]


app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser


@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello hey': name})
    return response


# # @app.route('/api/person/<person_id>')
# @app.route('/api/person/<int:person_id>')  # 类型转换
# def person(person_id):
#     response = jsonify({'Hello': person_id})
#     return response


if __name__ == '__main__':
    print(app.url_map)
    app.run()
