from flask import Flask, redirect, render_template, request, url_for
import json, requests
from twit import twit

import plotly.plotly as py
import plotly.graph_objs as go
import plotly

app = Flask(__name__)

def plotpie():
    labels = ['Positive', 'Negative', 'Neutral']
    values = [18, 7, 5]
    colors = ['#87F971', '#F24D4D', '#70ABEA']
    trace = go.Pie(labels=labels, values=values)
    layout = go.Layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    return plotly.offline.plot(go.Figure(data=[trace], layout=layout), output_type="div")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    #grabs the keyword from the form
    # keyword = request.form['key_word']
    # searchTwit = twit()
    # twit.search(keyword)
    return render_template('graph.html', chart=plotpie())

