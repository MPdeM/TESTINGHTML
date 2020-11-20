from flask import Flask, render_template, request

app = Flask(__name__)

# by default method is "get" but to increase privacy "POSt"
# for get-> request.args.get for post -> request.form.get
@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        return render_template("greet.html", name = request.form.get("name", "world!"))