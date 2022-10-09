from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = "myPassword"

@app.route('/')
def pageForm():
    return render_template("index.html")

@app.route('/process',methods=["POST"])
def processForm():
    session["yourName"] = request.form["Name"]
    session["yourLocation"] = request.form["locations"]
    session["yourFavoriteLanguage"] = request.form["Languages"]
    session["yourComments"] = request.form["Comments"]
    return redirect('/result')

@app.route('/result')
def returnedForm():
    return render_template("result.html")

if __name__=="__main__":       
    app.run(debug=True)    

