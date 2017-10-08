import re
from flask import Flask, render_template, redirect, request, flash, session
from datetime import datetime


app = Flask(__name__)
app.secret_key = "YouAreGreat"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def process():
    info_dict = request.form
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    email_add = request.form['email_add']
    birth_day = request.form['birthDay']
    pass_word = request.form['passWord']
    pass_word_confirm = request.form['passWordConf']
    # making regex objects https://docs.python.org/3.1/library/re.html
    date_match = re.compile(r"(0[1-9]|1[012])[/](0[1-9]|[12][0-9]|3[01])[/](19|20)\d\d$")
    pass_match = re.compile(r"(?=.*[A-Z])(?=.*\d).{8,}$")
    email_match = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    name_match = re.compile(r"[a-zA-z]+$")
    input_valid = True

    # for key, value in info_dict.items():
    #     print(key, value)
    for key, value in info_dict.items():
        if len(value) == 0:
            input_valid = False
            flash("The {} cannot be blank.".format(key))
    # if there are not blanks
    if input_valid:
        # check against the patterns we created
        if not re.match(name_match, first_name):
            input_valid = False
            flash("The first name must be only letters.")
        if not re.match(name_match, last_name):
            input_valid = False
            flash("The last name must be only letters.")
        if not re.match(email_match, email_add):
            input_valid = False
            flash("The email address is not valid.")
        if pass_word != pass_word_confirm:
            input_valid = False
            flash("The password and confirmation do not match")
        if not re.match(pass_match, pass_word):
            input_valid = False
            flash("The password must include at least 8 characters long inluding one UPPER case letter and one digit")
        if not re.match(date_match, birth_day):
            input_valid = False
            flash("The date is not in the correct MM/DD/YYYY format")
        else:
            # make sure birthday is in the past
            birth_day_object = datetime.strptime(birth_day, '%m/%d/%Y')
            if datetime.now() < birth_day_object:
                input_valid = False
                flash("How can you enter information if you aren't born yet?")

    if input_valid:
        flash("Thanks for submitting your information")
    return redirect('/')

app.run(debug=True)
