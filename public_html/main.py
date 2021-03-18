import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='NutrenApp')

@app.route('/', methods=["GET","POST"])
def calculate_imc():
    if request.method == "POST":
        info = request.form
        weight = int(info['weight'])
        height = int(info['height'])

        imc = weight / np.square(height/100)
        
        return render_template('show.html', imc = imc)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
