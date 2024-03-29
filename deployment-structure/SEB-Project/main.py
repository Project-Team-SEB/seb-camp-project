import datetime

from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    return render_template('index.html')


@app.route('/about')
def about_us():

    return render_template('aboutus.html')

@app.route('/featured')
def featured():

    return redirect('/')

@app.route('/form')
def form():

    return render_template('form.html')


@app.route('/contact')
def contact():

    return render_template('contact.html')


# function to add to JSON

@app.route('/add_data', methods=['POST'])
def add_data():
    Longitude = request.form['Longitude']
    Latitude = request.form['Latitude']
    Name = request.form['Name']
    Object_type = request.form['Object type']
    

    data = {
        'Name': Name,
        'Object type': Object_type,
        'Latitude': float(Latitude), 
        'Longitude': float(Longitude)
                              
        }
    
    with open ('static/map/dane1.json', 'r', encoding='utf-8') as file:
        exsisting_data = json.load(file)

    exsisting_data.append(data)
     
    with open('static/map/dane1.json', 'w' , encoding='utf-8') as file:
        json.dump(exsisting_data, file, indent=4)
        file.write('\n')

    return redirect('/')
    
if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
