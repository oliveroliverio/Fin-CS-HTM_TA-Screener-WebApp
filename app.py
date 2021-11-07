from flask import Flask, render_template
from patterns import patterns
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def helloWorld():
  return render_template('index.html', patterns=patterns)

@app.route('/snapshot')
def snapshot():
  with open('datasets/companies.csv') as f:
    companies = f.read().splitlines()
    for company in companies:
      symbol = company.split(',')[0]
      print(symbol)
  return {
    'code': 'success'
  }


# To run:
#   export FLASK_ENV=development
#   flask run
# Testing change on macbook pro