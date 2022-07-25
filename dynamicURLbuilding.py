from flask import Flask, redirect, url_for

# redicrect to redirect the page, url_for for building the url dynamically

app = Flask(__name__)


@app.route('/success/<int:score>')  # string by default
def success(score):
    return "<html><h1>The person has passed with score " + str(score) + ", Congratulations!</h1></html>" # html etc can be embedded too, better to use external type 


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed with score " + str(score) + ", good luck!"


@app.route('/')
def welcome():
    return 'Welcome to the result page'


@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks >= 34:
        result = 'success' # will head to decorator with url 'pass'
    else:
        result = 'fail'  # will head to decorator with url 'fai'
    return redirect(url_for(result, score=marks))


if __name__ == '__main__':
    app.run(debug=True)
