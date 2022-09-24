# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import pathlib
import webbrowser
## data okuma
path = pathlib.Path(__file__).parent.absolute()
df = pd.read_excel(str(path)+"/dataset.xlsx")
data = df.values


## data normalize
jobs = ["AI Software Engineer",
            "Mathematician",
            "Embedded Software Junior Engineer",
            "Embedded Software Med Level Engineer",
            "Embedded Software Senior Engineer",
            "Web Developer Junior",
            "Web Developer Med Level",
            "Web Developer Senior",
            "Display artist",
            "Artist",
            "Trader",
            "Civil Engineer",
            "Team Leader"          
            ]

for i in data:
    job = i[-1]
    indis = jobs.index(job)
    i[-1] = indis

X = data[:,:12]
Y = data[:,12]
Y=Y.astype('int')
X=X.astype('int')

## DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model = model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


## RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

model2=RandomForestClassifier(n_estimators=42)

model2.fit(X_train,y_train)

y_pred=model2.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        edu = int(request.form['edu'])
        cre = int(request.form['cre'])
        ana = int(request.form['ana'])
        sor = int(request.form['sor'])
        hes = int(request.form['hes'])
        lid = int(request.form['lid'])
        ikna = int(request.form['ikna'])
        bil = int(request.form['bil'])
        yaz = int(request.form['yaz'])
        cin = int(request.form['cin'])
        tec = int(request.form['tec'])
        ort = int(request.form['ort'])
        user_data = [edu,cre,ana,sor,hes,lid,ikna,bil,yaz,cin,tec,ort]
        user_data = np.array(user_data)
        user_data = user_data.reshape(1, -1)
        pred = model.predict(user_data)
        return jobs[pred[0]]
    else:
        return render_template("index.html")

if __name__ == "__main__":
    webbrowser.open("http://localhost:5000")
    app.run(debug=True)
