from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
  return 'hello world'


# be sure to run
# export FLASK_ENV=development
