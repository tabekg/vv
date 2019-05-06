import os

from flask import jsonify, request
from app import create_app
from app.services import call

config_name = 'development'
app = create_app(config_name)

@app.route('/api/<string:version>/<string:path>.<string:name>', methods=['GET', 'POST'])
def index(version, path, name):
    data = request.get_json(force=True)
    response = call(path, name, version, data)
    return jsonify(response[0]), response[1]

if __name__ == '__main__':
    app.run(debug=True)
