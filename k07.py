from flask import Flask, render_template, request, session
import os

app = Flask (__name__)  
app.secret_key = os.urandom(32)

username = "bob"
password = "bobbins"

@app.route("/")
def hello_world():
    print "\n\n"
    print "Cookie username: ", session.get('username')
    print "Cookie password: ",session.get('password')
    if session.get('username') == username and session.get('password') == password:
        return render_template('greet.html',user=session.get('username'))
    else:
        return render_template( 'login.html' )

@app.route("/greet")
def greet():
    print "\n\n"
    print "Form username: ", request.args.get('username')
    print "Form password: ", request.args.get('password')
    session['username'] = request.args.get('username')
    session['password'] = request.args.get('password')
    if session.get('username')== username and session.get('password')==password:
        return render_template( 'greet.html', user = session.get('username') )
    else:
        return render_template('error.html')

@app.route("/logout")
def logout():
    session.pop("username")
    session.pop("password")
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True;
    app.run()
