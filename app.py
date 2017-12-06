'''
Secret Santa csDojo
'''
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils import auth, database

app = Flask(__name__)
#for sessions
app.secret_key = os.urandom(32)

#base 
@app.route("/")
def start():
    return render_template("base.html")

#login authentication
@app.route('/login', methods=['GET', 'POST'])
def authentication():
    # if user already logged in, redirect to profile
    if session.get('username'):
        return redirect('profile')
    # user entered login form
    elif request.form.get('login'):
        return auth.login()
    # user didn't enter form
    else:
        return render_template('login.html', title = "Login")

@app.route('/create', methods=['GET', 'POST'])
def create():
    # if user already logged in, redirect to profile
    if session.get('username'):
        return redirect('profile')
    else:
        return redirect('login')

@app.route("/profile")
def profile():
    flash("PROFILE!")
    return render_template('profile.html', title="IN")

    
if __name__ == "__main__":
    app.debug = True
    app.run()
