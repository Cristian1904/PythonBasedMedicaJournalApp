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
    return render_template('about.html')

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

def get_recommendations(sickness):
    # Define a function to read recommendations from a file based on the selected sickness
    target_folder = 'sickness_recommendations'
    file_path = os.path.join(target_folder, f'{sickness}.txt')
    try:
        with open(file_path, 'r') as file:
            recommendations = file.readlines()
            if not recommendations:
                return "No recommendations available for this sickness."
            return recommendations
    except FileNotFoundError:
        return "No recommendations available for this sickness."
    except Exception as e:
        return f"An error occurred: {str(e)}"
@app.route('/sickness', methods=['GET', 'POST'])
@app.route('/sickness', methods=['GET', 'POST'])
def sickness():
    selected_sickness = None
    recommendations = None

    if request.method == 'POST':
        selected_sickness = request.form.get('sickness')
        print(f"Selected sickness: {selected_sickness}")
        recommendations = get_recommendations(selected_sickness)
        print(f"Final recommendations: {recommendations}")

    if recommendations is None:
        recommendations = ['No recommendations available for this sickness.']

    return render_template('sickness.html', selected_sickness=selected_sickness, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
