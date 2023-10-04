import requests
import json
from flask import Flask
text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
currencies = json.loads(text)
#print(currencies['Valute'])
for currency in currencies['Valute']:
    print(currency)


app = Flask(__name__)


@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(text)
    result = ''
    for currency in currencies['Valute']:
        result += str(currency) + '<br>'
    result = text
    return result



if __name__ == "__main__":
    app.run()