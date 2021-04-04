from sortedcontainers import SortedDict
import datetime
from datetime import date
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    now=datetime.datetime.now()
    friends={"Govind":abs((datetime.date.today()-datetime.date(2021,10,1)).days),
             "Lokesh":abs((datetime.date.today()-datetime.date(2021,5,31)).days),
             "Bharat":abs((datetime.date.today()-datetime.date(2021,6,10)).days),
             "Chhotu":abs((datetime.date.today()-datetime.date(2021,6,19)).days),
             "Sanjay":abs((datetime.date.today()-datetime.date(2021,1,11)).days),
             "Yashwanth":abs((datetime.date.today()-datetime.date(2021,9,6)).days),
             "Vaibhav":abs((datetime.date.today()-datetime.date(2021,12,6)).days)
             }
    Friends=SortedDict({v:i for i,v in friends.items()})
    comingup=Friends[min(Friends.keys())]
    birthday=now.month==9 and now.day==6
    return render_template("index.html",birthday=birthday,Friends=Friends,comingup=comingup)
