from flask import Flask, render_template, request
import logging

app = Flask(__name__)

fixtures = [
    (1, 'Burnley', 'Man City', '2023-08-11T19:00:00Z'),
    (1, 'Arsenal', "Nott'm Forest", '2023-08-12T11:30:00Z'),
    (2, 'Bournemouth', 'West Ham', '2023-08-12T14:00:00Z'),
    (2, 'Brighton', 'Luton', '2023-08-12T14:00:00Z'),
    (3, 'Everton', 'Fulham', '2023-08-12T14:00:00Z'),
    (3, 'Sheffield Utd', 'Crystal Palace', '2023-08-12T14:00:00Z'),
    (4, 'Newcastle', 'Aston Villa', '2023-08-12T16:30:00Z'),
    (4, 'Brentford', 'Spurs', '2023-08-13T13:00:00Z'),
    (5, 'Chelsea', 'Liverpool', '2023-08-13T15:30:00Z'),
    (5, 'Man Utd', 'Wolves', '2023-08-14T19:00:00Z')
]

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/gameweeks', methods=['GET', 'POST'])
def gameweeks():
    if request.method == 'POST':
        selected_gameweek = int(request.form.get('gameweek'))
        selected_fixtures = [f for f in fixtures if f[0] == selected_gameweek]
        return render_template('gameweeks.html', fixtures=selected_fixtures)
    return render_template('gameweeks.html', fixtures=fixtures)

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
