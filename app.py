from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Telegrambot'

if __name__ == "_main_":
    app.run()