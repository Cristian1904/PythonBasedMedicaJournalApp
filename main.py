import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['APPLICATION_ROOT'] = '/'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', home_link=home)

@app.route('/jurnal', methods=['GET', 'POST'])
def jurnal():
    if request.method == 'POST':
        selected_date = request.form['selectDate']
        activities = request.form['activities']
        meals = request.form['meals']
        health_status = request.form['health']

        # Obține calea către directorul scriptului curent
        target_folder = 'jurnal_zilnic'

        file_name = f"DATA_{selected_date}.txt"
        file_path = os.path.join(target_folder, file_name)
        
        # Scrie datele în fișierul text
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"Data: {selected_date}\n")
            file.write(f"Activități fizice: {activities}\n")
            file.write(f"Mese: {meals}\n")
            file.write(f"Starea de sănătate: {health_status}\n\n")
    return render_template('jurnal.html')

if __name__ == '__main__':
    app.run(debug=True)
