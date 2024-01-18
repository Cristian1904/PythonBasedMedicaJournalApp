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
    target_folder = 'sickness_recommendations'
    file_path = os.path.join(target_folder, f'{sickness}.txt')
    try:
        with open(file_path, 'r') as file:
            recommendations = file.readlines()
            if not recommendations:
                return None
            return recommendations
    except FileNotFoundError:
        return None
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_report(date):
    target_folder = 'healthcare'
    file_path = os.path.join(target_folder, f'{date}.txt')
    try:
        with open(file_path, 'r') as file:
            report = file.readlines()
            if not report:
                return None
            return report
    except FileNotFoundError:
        return None
    except Exception as e:
        return f"An error occurred: {str(e)}"    
@app.route('/sickness', methods=['GET', 'POST'])
def sickness():
    selected_sickness = None
    recommendations = None

    if request.method == 'POST':
        selected_sickness = request.form.get('sickness')
        recommendations = get_recommendations(selected_sickness)
        
    if recommendations is None:
        recommendations = ['No recommendations available for this sickness.\\n']

    return render_template('sickness.html', selected_sickness=selected_sickness, recommendations=recommendations)

@app.route('/health', methods=['GET', 'POST'])
def health():
    if request.method == 'POST':
        selectDate = request.form.get('selectDate')
        activities = request.form.get('activities')
        mood = request.form.get('mood')
        sleep = request.form.get('sleep')
        water = request.form.get('water')
        symptoms = request.form.getlist('symptoms')
        vitalSigns = request.form.get('vitalSigns')
        exerciseIntensity = request.form.get('exerciseIntensity')
        moodTracker = request.form.get('moodTracker')
        painScale = request.form.get('painScale')
        allergies = request.form.getlist('allergies')

        target_folder = 'healthcare'
        file_name = f"{selectDate}.txt"
        file_path = os.path.join(target_folder, file_name)

        # Save form data to a text file inside the folder
        with open(file_path, 'a') as file:
            file.write(f"Date: {selectDate}\n")
            file.write(f"Activities: {activities}\n")
            file.write(f"Mood: {mood}\n")
            file.write(f"Sleep: {sleep} hour/s\n")
            file.write(f"Water: {water}\n")
            file.write(f"Symptoms: {', '.join(symptoms)}\n")
            file.write(f"Vital Signs: {vitalSigns}\n")
            file.write(f"Exercise Intensity: {exerciseIntensity}\n")
            file.write(f"Mood Tracker: {moodTracker}\n")
            file.write(f"Pain Scale: {painScale}\n")
            file.write(f"Allergies: {', '.join(allergies)}\n")
            file.write('\n')  # Add a separator for each entry


    return render_template('health.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
    report = None
    date = None
    if request.method == 'POST':
        date = request.form.get('selectDate')
    report = get_report(date)
    return render_template('view.html', report=report)


if __name__ == '__main__':
    app.run(debug=True)
