from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('noturtle.html')

@app.route('/ninja')
def all_turtles():
    return render_template('index.html', img_name='tmnt.png')

@app.route('/ninja/<ninja_color>')
def turtle(ninja_color):
    if ninja_color == 'red':
        img_filename = 'raphael.jpg'
    elif ninja_color == 'blue':
        img_filename = 'leonardo.jpg'
    elif ninja_color == 'purple':
        img_filename = 'donatello.jpg'
    elif ninja_color == 'orange':
        img_filename = 'michelangelo.jpg'
    else:
        img_filename = 'notapril.jpg'
    return render_template('index.html', img_name=img_filename)

app.run(debug=True)
