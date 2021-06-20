from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import json

import os

app = Flask(__name__)

with open('data.json', 'r') as f:
    data=f.read()
data = json.loads(data)
f.close()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/farmer/<int:index>')
def farmer(index):
    return render_template('individualfarmer.html',data=data[index])

@app.route('/newfarmer',methods=['POST','GET'])
def newfarmer():
    if request.method=='POST':
        name = request.form['name']
        bname = request.form['bname']
        desc = request.form['desc']
        org = request.form['org']
        chem = request.form['chem']
        farmm = request.form['farmm']
        price = request.form['price']
        prod = request.form['prod']
        newvendor={"name":name,"bname":bname,"description":desc,"is_organic":org,"farmming_method":farmm,"is_chemical":chem,"price":price,"produce":prod}

        data.append(newvendor)
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
    return render_template('newvendor.html')




@app.route('/gallery')
def gallery():
    # collection = db.vendors
    # data = list(collection.find())
    # print(data)
    return render_template('galleryscreen.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
