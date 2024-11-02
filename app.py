from flask import Flask, render_template, request, jsonify
import csv
import os
import random

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form.get('n', 0))
        fib_sequence = compute_fibonacci(n)
        return jsonify(fib_sequence)
    return render_template('fibonacci.html')

def compute_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

@app.route('/csv', methods=['GET', 'POST'])
def csv_reader():
    csv_file_path = './resource/data.csv'
    csv_data = []

    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                csv_data.append(row)

    if request.method == 'POST':
        new_entry = [
            request.form['id'],
            request.form['F_Name'],
            request.form['L_Name'],
            request.form['email'],
            request.form['email2'],
            request.form['profesi']
        ]
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_entry)
        
        csv_data.append(new_entry)

    return render_template('csv_reader.html', csv_data=csv_data)

if __name__ == '__main__':
    app.run(debug=True)