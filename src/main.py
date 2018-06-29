from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f"Given username is: {request.values['username']}"
    else:
        html_form = """
            <form method="POST" action="/login">
                <input name="username" type="text" />
                <input type="submit" value="Send" />
            </form>
        """
        return html_form

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)