from flask import Flask, render_template

app = Flask(__name__)

client = {
    'has_login': False,
    'name': 'Gustavo'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', client=client)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)