from flask import Flask, request, render_template,url_for
app = Flask(__name__, static_folder='static')

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()