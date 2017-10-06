from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'hahasosmart'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] = int(session['counter']) + 1
    return render_template('index.html')

@app.route('/count2', methods=['POST'])
def add_two():
    session['counter'] = int(session['counter']) + 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
