from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/play/<int:num>")
def play_num(num):
    return render_template("play_x.html", num1=num)

@app.route("/play/<int:num>/<string:color>")
def play_num_color(num, color):
    return render_template("play_x_color.html", num2=num, color=color)


if __name__=="__main__":
    app.run(debug=True)