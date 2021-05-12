import flask as fs

app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def menu():
    return fs.render_template('login.html')


@app.route('/<username>/menu')
def login(username=None):
    return fs.render_template('menu.html', username=username)


app.run(host='0.0.0.0', port=1000)
