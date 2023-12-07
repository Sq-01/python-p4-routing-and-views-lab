#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#Index view at base url
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

#print string view
@app.route('/print/<string:text>')
def print_string(text):
    print(text)   #printing on console
    return f'hello'   #Browser display

#count view
@app.route('/count/<int:num>')
def count(num):
    return '\n'.join(str(i) for i in range(num)) + '\n'

#math view
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else: 
        result = "Invalid operation"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
