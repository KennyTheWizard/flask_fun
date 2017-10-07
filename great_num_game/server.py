from flask import Flask, redirect, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "Imawizard"

@app.route('/')
def index():
    if 'sec_num' not in session:
        session['sec_num'] = random.randint(1, 100)
    if 'guessed' not in session:   
        session['hintBox'] = 'hintBoxWrong'
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    the_guess = int(request.form['number'])
    if the_guess == session['sec_num']:
        session['hint'] = "{} was the number!".format(the_guess)
        session['guessed'] = True
        session['hintBox'] = 'hintBoxRight'
    elif the_guess < session['sec_num']:
        session['hint'] = "Too Low!"
    elif the_guess > session['sec_num']:
        session['hint'] = "Too High!"
    return redirect('/')
    
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)