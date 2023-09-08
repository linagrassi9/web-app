from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
users = {
    'test': {
        'username': 'test',
        'password': generate_password_hash('test'),
    }
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists', 'error')
        else:
            users[username] = {
                'username': username,
                'password': generate_password_hash(password)
            }
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            flash('Login successful!', 'success')
            return redirect(url_for('bill_submission'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/bill_submission', methods=['GET', 'POST'])
def bill_submission():
    if request.method == 'POST':
        supplier_name = request.form['supplier_name']
        registration_number = request.form['registration_number']
        bill_amount = request.form['bill_amount']
        bill_date = request.form['bill_date']
        delivery_date = request.form['delivery_date']

        flash('Bill submitted successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('bill_submission.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)