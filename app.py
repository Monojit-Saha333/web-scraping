#doing imports
from flask import Flask,render_template,request,jsonify
from flask_cors import  CORS,cross_origin
import requests
from urllib.request import  urlopen as uReq
import pymongo
import pandas as pd
import crawler
import datamanage
import pandas as pd
app=Flask(__name__) #initializing flaskapp

@app.route("/",methods=['GET','POST'])
def index():
   return render_template('scrape.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        search_string = request.form['content'].replace(' ', '')
        #print(search_string)
        try:
            collection_present=datamanage.check_collection(search_string)
            #print(collection_present)
            if collection_present == True:
                records = datamanage.fetch_records(collection_name=search_string)
                return render_template('result.html',reviews=records)
            else:
                all_records=crawler.obtain_product_reviews(search_string)
                c = datamanage.create_collection_insert_records(collection_name=search_string, records=all_records)
                return render_template('result.html',reviews=all_records)
        except Exception as e:
            return render_template('exception.html')

    else:
        return render_template('scrape.html')


if __name__=="__main__":
    app.run(port=800,debug=True)

