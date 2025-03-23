from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Deploying Flask App at Vercel, I did! Wissam did it with the help of Umar and Saad'

if __name__ == '__main__':
    app.run(debug=True)
