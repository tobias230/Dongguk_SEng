import pandas as pd
from flask import Flask
app = Flask(__name__)

df = pd.read_csv('user.csv')


@app.route('/')
def index():
    username = "newUserName"
    password = "newPassword"

    df.append([username, password])
    df.to_csv('user.csv', index=False)
    return "New user added"


if __name__ == '__main__':
    app.run(debug=True)
