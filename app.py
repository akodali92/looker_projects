# python imports
from flask import Flask, render_template

# project imports


# initialize app
app = Flask(__name__)

# setup routes
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

# run app
if __name__ == '__main__':
    app.run(debug=True)
