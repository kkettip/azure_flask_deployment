from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

df = pd.read_json('https://data.cms.gov/data-api/v1/dataset/939226be-b107-476e-8777-f199a840138a/data')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )