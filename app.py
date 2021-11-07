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
      df = yf.download(symbol, start="2021-01-01", end="2021-10-01")
      df.to_csv('datasets/daily/{}.csv'.format(symbol))
  return {
    'code': 'success'
  }


# To run:
#   export FLASK_ENV=development
#   flask run
# Testing change on macbook pro