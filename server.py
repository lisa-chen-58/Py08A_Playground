from flask import Flask, render_template, redirect

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return redirect("/play")


# When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes. Please use a template to render this.
@app.route("/play")
def index():
    num = 0
    return render_template("index.html", num = num)


# When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times. 
@app.route("/play/<int:num>")
def number(num):
    return render_template("index.html", num = num)

# When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color).
@app.route("/play/<int:num>/<string:color>")
def number(num,color):
    print (color)
    return render_template("index.html", num = num, color=color)

if __name__== "__main__":
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform