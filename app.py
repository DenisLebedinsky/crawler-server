
from flask_cors import CORS
from flask import request
from flask import Flask
from flask import jsonify
from flask import abort
import os
import json
import controller

os.environ["PORT"] = "5000"

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/videos/<id>', methods=['GET'])
def videoDetails(id):
    try:
        data = controller.findById(id)
        if not data:
            raise Exception('not found')
        res = {
            "id": id,
            "name": data['name'],
            "likes": data['likes'],
            "dislikes": data['dislikes'],
            "views": data['views'],
            "subscribers": data['subscribers'],
            "url": data['url']
        }
    except:
        res = {}
    return jsonify(res)


@app.route('/api/videos/info/', methods=['GET'])
def videoInfo():
    try:
        res = controller.startCrawling(request.args.get('url'))
    except NameError:
        res = {}
    return jsonify(res)


@app.route('/api/videos', methods=['POST'])
def videoDetailsPost():
    data = request.get_json()
    res = controller.save(data)
    return res, 201


@app.errorhandler(500)
def server_error(e):
    return """
   error: {}
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ["PORT"], debug=True)
