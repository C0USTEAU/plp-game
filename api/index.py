from flask import Flask, render_template, request
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def root():
    return render_template('root.html')

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
