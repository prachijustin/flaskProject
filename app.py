from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello and welcome to Flask</h1>'


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:   #if POST
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'praachi' and password == 'sharma':
            return render_template('logout.html', name=name)
        else:
            return 'Invalid credentials!'


@app.route('/nagarro')
def nagarro_intro():
    return render_template('nagarro.html')


if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)

