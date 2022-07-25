# integrate html with flask
# aka jinja2 technique


# building url dynamically
# variable rules and url building
from flask import Flask, redirect, url_for, render_template, request
# request - get n post
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
# my result checker html page after submit is done
def submit():
    total_score = 0
    if request.method == 'POST':  # jo form me tha post
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])  # arg me ids he
        total_score = (science + maths + c + data_science) / 4
    res = ""
    if total_score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', key=total_score, value=res)

# it ll generate a dynamic url


if __name__ == '__main__':
    app.run(debug=True)



