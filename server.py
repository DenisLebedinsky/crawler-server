
from flask_cors import CORS
from flask import request
from flask import Flask
from flask import jsonify
import os 


os.environ["PORT"] = "123123"

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api', methods=['POST'])
def spacyAnalysis():
		note = request.json['text']	
		print(os.environ["MONGODB_URI"])
		return note


@app.route('/', methods=['GET'])
def getQuery():
  
    return "Get query work"


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ["PORT"] , debug=True)

