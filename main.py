
from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'  # Replace with your preferred server name and port
app.config['APPLICATION_ROOT'] = '/'

def get_url(target):
   with app.app_context():
      return url_for(target)




posts = [
   {
      'author': 'Cristi',
      'title': 'Marian',
      'content':'First post content',
      'date': 'April 2020, 1999'
   },
   {
      'author': 'Ruxi',
      'title': 'ION liviu rebreanu',
      'content': 'Second post content',
      'date': 'April 2020, 2003'
   }
]

@app.route('/')
@app.route('/home')
def home():
   about = get_url('about')
   jurnal = get_url('jurnal')
   return render_template('home.html', posts = posts, about_link = about, jurnal_link = jurnal)

@app.route('/about')
def about():
   home = get_url('home')
   return render_template('about.html', posts = posts, home_link = home)

@app.route('/jurnal')
def jurnal():
   jurnal = get_url('jurnal')
   return render_template('jurnal.html', posts = posts, jurnal_link = jurnal)

if __name__ == '__main__':
   app.run(debug=True)