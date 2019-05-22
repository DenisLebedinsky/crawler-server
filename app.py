
from flask_cors import CORS
from flask import request
from flask import Flask, send_from_directory, send_file
from flask import jsonify
import os
import controller


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def root():
    return send_file('static/index.html')

@app.route('/api/videos', methods=['GET'])
def videosList():
    return jsonify(controller.getList(request.args))


@app.route('/api/videos/<id>', methods=['GET'])
def videoDetails(id):
    return jsonify(controller.findById(id))


@app.route('/api/videos/info/', methods=['GET'])
def videoInfo():
    return jsonify(controller.startCrawling(request.args.get('url')))


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
    app.run(host=os.environ["HOST"], port=os.environ["PORT"], debug=False)
