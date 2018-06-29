from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    import pdb; pdb.set_trace()
    i = 3
    i += 1
    visited = i
    return "You've visited " + str(visited) + " times"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
