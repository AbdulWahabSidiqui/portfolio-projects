import os

from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
URL = "https://www.alphavantage.co/query"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    stock_data = None

    if request.method == 'POST':

        symbol = request.form['symbol']

        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY,
        }

        response = requests.get(URL, params=parameters)
        data = response.json()

        daily_data = data["Time Series (Daily)"]

        latest_date = list(daily_data.keys())[0]

        latest_data = daily_data[latest_date]

        stock_data = {
            "symbol": symbol,
            "date": latest_date,
            "open": latest_data["1. open"],
            "high": latest_data["2. high"],
            "low": latest_data["3. low"],
            "close": latest_data["4. close"],
            "volume": latest_data["5. volume"],
        }

    return render_template('index.html',stock=stock_data)

if __name__ == '__main__':
    app.run(debug=True)







