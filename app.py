from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate(a, c, operation):
    a, b = float(a), float(b)
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")

@app.route('/calculate', methods=['POST'])
def calc_route():
    data = request.json
    try:
        result = calculate(data['a'], data['b'], data['operation'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
