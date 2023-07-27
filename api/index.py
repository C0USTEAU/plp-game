from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        passphrase = request.form.get('passphrase')
        if not passphrase:
            error_msg = 'Please enter Passphrase!'
            return render_template('index.html', error_msg=error_msg)
        else:
            return render_template('index.html', passphrase=passphrase)
    return render_template('templates/index.html')
