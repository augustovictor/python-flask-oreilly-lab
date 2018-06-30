from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = 'MY-SECRET'

@app.route('/welcome')
def welcome(name=None):
    username = request.cookies.get('username')
    if username:
        return render_template('hello.html', name=username)
    else:
        flash('You are not logged in')
        return redirect(url_for('signin'))

@app.route('/login', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            flash('Successfully logged in')
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', username)
            return response
            
        else:
            flash('Invalid credentials')
    return render_template('login.html')

def valid_login(username, password):
    return username == password

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('signin')))
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)