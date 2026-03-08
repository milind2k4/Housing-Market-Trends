from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
