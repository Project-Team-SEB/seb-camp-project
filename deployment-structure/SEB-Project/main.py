import datetime

from flask import Flask, request, render_template

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

    return render_template('featured.html')

@app.route('/form')
def form():

    return render_template('form.html')


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
