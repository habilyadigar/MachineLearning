from flask import Flask, render_template, request
import json
from tahminData import tahmin

app = Flask(__name__,template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    if request.method == "POST":
        print(request.form)
        tahminData = {}
        for x in request.form:
            tahminData[x] = [int(request.form[x])]
        print(tahminData)
        data = tahmin(tahminData)
        data = round(data,2)
        print(data)
        
        return render_template('index.html',data=data)
    return render_template('index.html')

#SERVİS OLARAK
@app.route('/api/predict', methods=['POST'])
def forapi():
    if request.method == "POST":
        data = tahmin(request.json)
        data = round(data,2)
        return str(data)
    return "ERROR DETECTED"

app.run(debug=True)