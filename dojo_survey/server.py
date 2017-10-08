from flask import Flask, render_template, redirect, request, flash, session

app = Flask(__name__)
app.secret_key = "YouAreGreat"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def process():
    name=request.form['name']
    location=request.form['location']
    fav_lang=request.form['fav_lang']
    comment=request.form['comment']
    input_valid = True

    if len(name) == 0:
        input_valid = False
        flash("The name cannot be blank.")
    if len(comment) == 0:
        input_valid = False
        flash("The commment field cannot be blank.")
    if len(comment) > 120:
        input_valid = False
        flash("The comment cannot be longer than 120 characters")

    if input_valid:
        session['name'] = name
        session['location'] = location
        session['fav_lang'] = fav_lang
        session['comment'] = comment
        return redirect('/resultspage')
    else:
        return redirect('/')

@app.route('/resultspage')
def show_results():
    return render_template('results.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)