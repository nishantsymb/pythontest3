import datetime
import random
from flask import Flask, render_template, request

app = Flask(__name__)

#Store Today's date in today
today = datetime.datetime.now()
givenInteger = int(today.strftime("%d"))

#Number Prefix Check
if (givenInteger%100==11 or givenInteger%100==12 or givenInteger%100==13):
    tempDaySuffix = "th"
elif (givenInteger%10==1):
    tempDaySuffix = "st"
elif(givenInteger%10==2):
    tempDaySuffix = "nd"
elif(givenInteger%10==3):
    tempDaySuffix = "rd"
else:
    tempDaySuffix = "th"

@app.route("/")
def index():
    image_url = f'https://picsum.photos/200/?random={random.random()}'
    return render_template('index.html',date=today.strftime("%d"),month=today.strftime("%B"),year=today.strftime("%Y"),daySuffix=tempDaySuffix,image_url=image_url)

@app.route("/about")
def about():
    return '<h1>About Page</h1>'

@app.route("/quotes")
def quotes():
    return '<h1>Here lies some quotes</h1>'