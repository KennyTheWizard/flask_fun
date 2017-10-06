from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def process():
    return render_template('results.html',
        name=request.form['name'], location=request.form['location'],
        fav_lang=request.form['fav_lang'], comment=request.form['comment'])

app.run(debug=True)