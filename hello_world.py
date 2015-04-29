
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    #return "Hello World!"
    return render_template('template.html')
  
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)