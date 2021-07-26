# python imports
from flask import Flask

# project imports


# initialize app
app = Flask(__name__)

# setup routes
@app.route("/")
def index():
    return "Hello World"

# run app
if __name__ == '__main__':
    app.run(debug=True)
