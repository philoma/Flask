from flask import Flask
#WSGI is a standard that helps communicate my application with web server
app=Flask(__name__)   #my app name object initialised with Flask


@app.route('/') # is a decorator, takes 2 parameters i.e. rules,options, string rules specify the url im gonna go in the web page
def welcome():
    return "Welcome to the website!"


@app.route('/members') #the above welcome() binding function should be dift than members in  '/members'
def members():
    return "Welcome To My YT podcasts"

if __name__=='__main__':
    app.run(debug=True) #if i pass debug=True, changes will reflect/commit on main page without explicitly restarting the server all over again.

