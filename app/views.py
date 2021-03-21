from app import app

@app.route("/")
def index():
    return "<h1>hello, you</h1>"

@app.route("/jinja")
def jinja():
    return render_template("/jinja.html")

@app.route("/x")
def redX():
    return "<h1 style='color : red'>X</h1>"