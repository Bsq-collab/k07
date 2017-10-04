from flask import Flask, render_template, request, session
import os

app = Flask (__name__)  
app.secret_key = os.urandom(32)

username = "bob"
password = "bobbins"

@app.route("/")
def hello_world():
    if request.cookies.get('username') == username and request.cookies.get('password') == password:
        greet()
    else:
        return render_template( 'login.html' )

@app.route("/greet")
def greet():
    print request.args.get('username')
    session['username'] = request.args.get('username')
    session['password'] = request.args.get('password')
    return render_template( 'greet.html', user = session['username'] )

if __name__ == "__main__":
    app.debug = True;
    app.run()
