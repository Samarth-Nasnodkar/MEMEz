from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
  return "Bot running"

def run():
  app.run(host="0.0.0.0", port=8080)

def start():
  t = Thread(target=run)
  t.start()