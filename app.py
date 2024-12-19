from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Dictionary of gifts with their descriptions
GIFTS = {
    'gift1': "professional personal masseur",
    'gift2': "your very own personal chef",
    'gift3': "COALS. you've been naughty",
    'gift4': "the fastest smallest peck"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name'].lower()
        if name == "katelyn bump":
            session['name_verified'] = True
            return redirect(url_for('birthday_check'))
        else:
            return redirect(url_for('merry_christmas'))
    return render_template('index.html')

@app.route('/birthday_check', methods=['GET', 'POST'])
def birthday_check():
    if not session.get('name_verified'):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        birthday = request.form['birthday']
        if birthday == "2005-03-20":  # Replace with actual birthday
            session['birthday_verified'] = True
            return redirect(url_for('gift_selection'))
        else:
            return render_template('birthday_check.html', error=True)
    return render_template('birthday_check.html', error=False)

@app.route('/gift_selection')
def gift_selection():
    if not session.get('birthday_verified'):
        return redirect(url_for('index'))
    return render_template('gift_selection.html')

@app.route('/reveal_gift/<int:gift_number>')
def reveal_gift(gift_number):
    if not session.get('birthday_verified'):
        return redirect(url_for('index'))
    
    gift_key = f'gift{gift_number}'
    selected_gift = GIFTS[gift_key]
    return render_template('final_gift.html', gift=selected_gift)

@app.route('/merry_christmas')
def merry_christmas():
    return render_template('merry_christmas.html')

if __name__ == '__main__':
    app.run(debug=True)