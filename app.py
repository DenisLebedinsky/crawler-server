
from flask_cors import CORS
from flask import request
from flask import Flask
import os
import controller

os.environ["PORT"] = "5000"

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/videos', methods=['GET'])
def videosList():
		return controller.getList(request.args)
   


@app.route('/api/videos/<id>', methods=['GET'])
def videoDetails(id):
    return controller.findById(id)

@app.route('/api/videos/info/', methods=['GET'])
def videoInfo():
    return controller.startCrawling(request.args.get('url'))


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
