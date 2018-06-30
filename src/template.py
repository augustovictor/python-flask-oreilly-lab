from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'MY-SECRET'

@app.route('/welcome/<name>')
def welcome(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            flash('Successfully logged in')
            return redirect(url_for('welcome', name=username))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

def valid_login(username, password):
    return username == password

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)