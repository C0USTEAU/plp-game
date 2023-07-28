from flask import Flask, render_template, request
import logging

app = Flask(__name__)

@app.route('/')
def root():
    logging.error("Rendering root template")
    return render_template('root.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    logging.error("Rendering start template")
    if request.method == 'POST':
        passphrase = request.form.get('passphrase')
        if not passphrase:
            error_msg = 'Please enter Passphrase!'
            return render_template('start.html', error_msg=error_msg)
        else:
            return render_template('start.html', passphrase=passphrase)
    return render_template('start.html')
