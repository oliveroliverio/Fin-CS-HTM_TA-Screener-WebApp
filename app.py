from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
  return 'hello world'

@app.route('/snapshot')
def snapshot():
  return {
    'code': 'sucess'
  }
# To run:
#   export FLASK_ENV=development
#   flask run