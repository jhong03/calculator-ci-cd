from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate(a, b, operation):
    a, b = float(a), float(b)
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
   
    else:
        raise ValueError("Invalid operation")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calc_route():
    if request.is_json:
        # API usage
        data = request.json
        try:
            result = calculate(data['a'], data['b'], data['operation'])
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        # Web form usage
        try:
            a = request.form['a']
            b = request.form['b']
            operation = request.form['operation']
            result = calculate(a, b, operation)
            return render_template('index.html', result=result)
        except Exception as e:
            return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
