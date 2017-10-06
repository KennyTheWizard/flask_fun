from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "supersecretinfo"

def janken_win(human_play, computer_play):
# 0 = rock, 1 = scissors, 2 = paper
    if human_play == 'rock':
        if computer_play == 1:
            session['wins'] += 1
            session['info'] = 'The computer played scissors, you played rock, YOU WIN!!!!!'
            session['result'] = 'win'
        elif computer_play == 2:
            session['losses'] += 1
            session['info'] = 'The computer played paper, you played rock, YOU LOSE :(:(:('
            session['result'] = 'lose'
        else:
            session['ties'] += 1
            session['info'] = 'The computer played scissors, you played scissors, tie :/'
    elif human_play == 'scissors':
        if computer_play == 1:
            session['ties'] += 1
            session['info'] = 'The computer played scissors, you played scissors, tie :/'
        elif computer_play == 2:
            session['wins'] += 1
            session['info'] = 'The computer played paper, you played scissors, YOU WIN!!!!!'
            session['result'] = 'win'            
        else:
            session['losses'] += 1
            session['info'] = 'The computer played rock, you played scissors, YOU LOSE :(:(:('
            session['result'] = 'lose'            
    else:
        if computer_play == 1:
            session['losses'] += 1
            session['info'] = 'The computer played scissors, you played paper, YOU LOSE :(:(:('
            session['result'] = 'lose'            
        elif computer_play == 2:
            session['ties'] += 1
            session['info'] = 'The computer played paper, you played paper, tie :/'
        else:
            session['wins'] += 1
            session['info'] = 'The computer played rock, you played paper, YOU WIN!!!!!'
            session['result'] = 'win'            

@app.route('/')
def index():
    if 'wins' not in session:
        session['wins'] = 0
    if 'losses' not in session:
        session['losses'] = 0
    if 'ties' not in session:
        session['ties'] = 0
    session.permanent=False
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_the_game():
    human_play = request.form['throw']
    computer_play = random.randint(0, 2)
    print(computer_play)
    janken_win(human_play, computer_play)
    return redirect('/')

app.run(debug=True)
