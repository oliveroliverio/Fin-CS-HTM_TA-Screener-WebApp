from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
  return render_template('index.html')

@app.route('/snapshot')
def snapshot():
  return {
    'code': 'sucess'
  }
# To run:
#   export FLASK_ENV=development
#   flask run