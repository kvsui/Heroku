from flask import Flask, render_template
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def landingpage():
	return(render_template("Main.html"))
@app.route('/Power')
def power():
	return render_template("Energy Sources.html")
@app.route('/visual')
def visual():
	return render_template("visual.html")
@app.route('/Data')
def data():
	df=pd.read_csv("file_02.csv")
	data_table=df.to_html()
	filepath = os.path.join('/Users/karanvirsingh/Desktop/flask/templates', 'index.html')
	text_file = open(filepath, "w")
	text_file.write(data_table)
	text_file.close()
	return render_template("index.html")
@app.route('/conservation')
def conservation():
	return render_template("conservation.html")	    
if __name__=="__main__":
	app.run(debug = True)