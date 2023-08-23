from flask import Flask, render_template
from forms import calcForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '163e34c5745bafbebe6e4c88794ab33f'

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'

@app.route("/calculator/add", methods=['GET','POST'])
def add():
    form = calcForm()
    flag = False
    res = 0
    if form.validate_on_submit():
        no1 = int(form.number1.data)
        no2 = int(form.number2.data)
        flag = True
        res = no1 + no2

    return render_template('calc.html', form = form, res=res, flag = flag)

@app.route("/calculator/subtract", methods=['GET','POST'])
def subtract():
    form = calcForm()
    flag = False
    res = 0
    if form.validate_on_submit():
        no1 = int(form.number1.data)
        no2 = int(form.number2.data)
        flag = True
        res = no1 - no2

    return render_template('calc.html', form = form, res=res, flag = flag)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
