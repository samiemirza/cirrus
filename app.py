from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = ' 588bd67857f4705303de0028'
API_URL = f'https://v6.exchangerate-api.com/v6/588bd67857f4705303de0028/latest/'


@app.route('/')
def index():
    return render_template('index.html')
 

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])
    
    # Fetch exchange rates
    response = requests.get(f'{API_URL}{from_currency}')
    data = response.json()
    
    if data['result'] == 'success':
        rate = data['conversion_rates'][to_currency]
        converted_amount = amount * rate
        return jsonify({
            'result': 'success',
            'converted_amount': converted_amount,
            'rate': rate
        })
    else:
        return jsonify({'result': 'error', 'message': data['error-type']})


if __name__ == '__main__':
    app.run(debug=True)



