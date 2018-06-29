from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return url_for('username', username='victor')

@app.route('/users/<username>')
def username(username):
    return f'Hello {username}'

@app.route('/posts/<int:post_id>')
def get_post(post_id):
    return 'Post ' + str(post_id)

@app.route('/hello')
def hello_world():
    # import pdb; pdb.set_trace()
    i = 3
    i += 1
    visited = i
    return "You've visited " + str(visited) + " times"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
