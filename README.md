# Fin-CS-HTM_TA-Screener-Webapp

Here's where I'll take notes on video.  Use other note apps sparingly (obsidian, evernote).  At least for coding projects.
[source](https://www.youtube.com/watch?v=OhvQN_yIgCo&t=1019s)
# Starting
## Adding templates to form in index.html
```html
  <form action="">
    <select name="pattern">
      {% for pattern in patterns %}
        <option value="{{pattern}}">{{patterns[pattern]}}</option>
      {% endfor %}
    </select>

    <input type="submit" value="scan">
  </form>
```

## Import yfinance package, S&P 500 companies csv list
- import yfinance package
- snapshot will take snapshot of the daily closes of all S&P500 stocks
- get list of S&P500 stocks [here](https://datahub.io/core/s-and-p-500-companies#resource-s-and-p-500-companies_zip) or [here, HTM version](https://github.com/hackingthemarkets/candlestick-screener/blob/master/datasets/symbols.csv)
  - created datasets directory and put this there.
- modified snapshot code to print each company from CSV file.  Be sure to go to `127.0.01:5000/snapshot` to trigger the console output

```python
@app.route('/snapshot')
def snapshot():
  with open('datasets/companies.csv') as f:
    symbols = f.read().splitlines()
    print(symbols)
  return {
    'code': 'success'
  }
```
- modified script to get just the symbols

```python
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
```
- now get each of these symbols from yf to get data given a start and end date
- then output data to it's own csv file under datasets directory (note: need to manually create the `daily` directory)

```python
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
```
- after downloading CSVs for each company, you then want to load each of these in a dataframe, then apply a TA-Lib candle stick pattern function to the DF, then see how it flags the last row (most recent), then we'll know if that pattern has appeared as of the close on that date.

# Working on main function
- go to `localhost:5000`
- click on dropdown, then scan.  What's happening is it's sent as a **query parameter**, which we can capture into a variable in flask.  Here we'll get some info about the **request**
- **request** contains info about the current request
  - ip address it came from
  - **post form variables**
  - here we'll get all the arguments: `pattern = request.args.get('pattern', None)` (which comes from the URL section in between `?` and `=`).  If not present, give it "none")

```python
@app.route('/')
def index():
  pattern = request.args.get('pattern', None)
  if pattern:
    print(pattern)
  return render_template('index.html', patterns=patterns)
```
- now run this by going to `localhost:5000`, click on dropdown, choose a pattern, click scan, note the console printing (note: remember to run in debug mode to see print console: `export FLASK_ENV=devlopment`)

