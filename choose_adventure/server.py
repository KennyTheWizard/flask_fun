from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    _title = "Start of an Adventure?"
    _content = "You come upon a simple man who just woke up. This man is going to work to start his day."
    _link1 = "/gowork"
    _link2 = "/nowork"
    _link1content = "He makes it to work"
    _link2content = "He doesn't"
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/gowork')
def gowork():
    _title = "He makes it to work"
    _content = "The man arrives at 8am and works till lunch."
    _link1 = "/eatsapple"
    _link2 = "/eatsandwich"
    _link1content = "He eats an apple for lunch."
    _link2content = "He eats a sandwich for lunch."
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content) 

@app.route('/eatsapple')
def eatsapple():
    _title = "He eats an apple."
    _content = "He feels peckish but continues his work. He notices something on the ground but he doesn't think much of it and finishes his work day."
    _link1 = "/goeshome"
    _link2 = "/goeshome"
    _link1content = "He drives home"
    _link2content = "He gets a ride home"
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)


@app.route('/eatsandwich')
def eatssand():
    _title = "He eats a sandwhich."
    _content = "He feels full and goes back to work satisfied. He notices something on the ground but doesn't think much of it and finishes his work day. "
    _link1 = "/goeshome"
    _link2 = "/goeshome"
    _link1content = "He drives home"
    _link2content = "He gets a ride home"
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/goeshome')
def goeshome():
    _title = "He arrives at home"
    _content = "He arrives at home, has a nice meal with his family and heads to bed."
    _link1 = "/"
    _link2 = "/"
    _link1content = "He goes to sleep."
    _link2content = "He laughs about something he remembered then goes to sleep."
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)    

@app.route('/nowork')
def nowork():
    _title = "He doesn't."
    _content = "He doesn't. He starts to wonder how long it has been since he missed a day of work and realizes he has gone to work every single day of his life. Except this day."
    _link1 = "/askhim"
    _link2 = "/dontaskhim"
    _link1content = "Ask him how feels about this."
    _link2content = "Do not engage this man."
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)    

@app.route('/askhim')
def askhim():
    _title = "Ask him how he feels about this."
    _content = "He tells you he's not sure. Somewhat disconcerted he asks, 'How are you?'"
    _link1 = "/good"
    _link2 = "/bad"
    _link1content = "'I'm fine.'"
    _link2content = "'I'm not so good.'"
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/good')
def good():
    _title = "He smiles wisely."
    _content = "He gives you a grin that shows years of reserve."
    _link1 = "/ask"
    _link2 = "/continue"
    _link1content = "'Do you know something I don't?'"
    _link2content = "'I am going to go home and rethink my life.'"
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/ask')
def ask():
    _title = "I know."
    _content = "I know that you were and always were going to say you felt good."
    _link1 = ""
    _link2 = ""
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/continue')
def cont():
    _title = "Farewell then."
    _content = "Farewell."
    _link1 = ""
    _link2 = ""
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)


@app.route('/bad')
def bad():
    _title = "He asks if he can help."
    _content = "'Is there anything I can do to make you feel better?'"
    _link1 = "/Yes"
    _link2 = "/No"
    _link1content = "'Yes.'"
    _link2content = "'No, thank you'"
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/Yes')
def Yes():
    _title = "Honesty check"
    _content = "He does everything in his power to make you feel better, so if you answered the last question honestly, you now feel better.'"
    _link1 = ""
    _link2 = ""
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/No')
def No():
    _title = "Sadly..."
    _content = "He wishes you fare travels and you go on your way."
    _link1 = ""
    _link2 = ""
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)


@app.route('/dontaskhim')
def dontaskhim():
    _title = "Don't engage the man."
    _content = "Together but unaware of your particulars you continue on together, but apart, in a state of remotely guided narrative."
    _link1 = "/studyfleck"
    _link2 = "/thermo"
    _link1content = "Study a fleck of dust on his wrist."
    _link2content = "Wonder about the properties of thermodynamics."
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content) 


@app.route('/thermo')
def thermo():
    _title = "The Universe is Expanding."
    _content = "Even though the universe is always expanding, entropy is always increasing, foretelling the end of the universe."
    _link1 = "/insight"
    _link2 = "/easier"
    _link1content = "Spend your life thinking about this and gaining insight."
    _link2content = "Think about something easier."
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/insight')
def insight():
    _title = "Gain insight"
    _content = "You got a +1 to your Perception!"
    _link1 = "/studyfleck"
    _link2 = "/thermo"
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)

@app.route('/easier')
def easier():
    _title = "FAIL!!!"
    _content = "You have failed."
    _link1 = "/studyfleck"
    _link2 = "/thermo"
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content) 



@app.route('/studyfleck')
def studyfleck():
    _title = "Open your mind to the infinite universe."
    _content = "While staring at the fleck, you feel fatigued."
    _link1 = "/pattern"
    _link2 = "/chaos"
    _link1content = ""
    _link2content = ""
    return render_template('index.html', title=_title, content=_content, link1=_link1, link2=_link2, link1_content=_link1content, link2_content=_link2content)


app.run(debug=True)

