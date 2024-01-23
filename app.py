from flask import Flask, request, render_template, request
import project
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/linktest')
def linktest():
    return render_template("checkpage.html")

@app.route('/result')
def result():
    urlname = request.args['name']
    result  = project.get_prediction_from_url(urlname)
    return result
@app.route('/faq')
def faq():
    return render_template("faq.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
