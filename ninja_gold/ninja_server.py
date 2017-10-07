import random
from datetime import datetime
from flask import Flask, request, redirect, render_template, session
from collections import defaultdict

app = Flask(__name__)
app.secret_key = "GroundControlToMajorTom"

@app.route('/')
def index():
    if 'goldCount' not in session:
        session['goldCount'] = 0
        session['activities'] = list()
    return render_template('ninja.html')

@app.route('/process_money', methods=['POST'])
def procces_money():
    building = request.form['building']
    money = 0
    act_dict = dict()
    if building == 'farm':
        money = random.randint(10, 20)
    elif building == 'cave':
        money = random.randint(5, 10)
    elif building == 'house':
        money = random.randint(2, 5)
    elif building == 'casino':
        money = random.randint(-50, 50)
    if building != 'casino':
        act_dict['class_name'] = 'mademoney'
        act_dict['content'] = 'Earned {} gold from the {}! ({})'.format(money,
                                                                        building, datetime.now())
    else:
        if money < 0:
            act_dict['class_name'] = 'lostmoney'
            act_dict['content'] = 'Entered a casino and lost {} gold... OUCH!! ({})'.format(
                abs(money), datetime.now())
        else:
            act_dict['class_name'] = 'mademoney'
            act_dict['content'] = 'Entered a casino and won {} gold... WOOHOO!! ({})'.format(
                money, datetime.now())
    # print(act_dict, session['activities'])
    session['activities'].append(act_dict)
    # print(session['activities'])
    session['goldCount'] += money
    return redirect('/')

app.run(debug=True)