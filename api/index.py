from flask import Flask, render_template, request
import logging

app = Flask(__name__)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/gameweeks', methods=['GET', 'POST'])
def gameweeks():
    return render_template('gameweeks.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        passphrase = request.form.get('passphrase')
        if not passphrase:
            error_msg = 'Please enter Passphrase!'
            return render_template('start.html', error_msg=error_msg)
        else:
            return render_template('start.html', passphrase=passphrase)
    return render_template('start.html')
