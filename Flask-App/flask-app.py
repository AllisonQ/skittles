from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
  return 'Hello World!'

@app.route('/boo')
def boo():
  return "I'm scared!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
