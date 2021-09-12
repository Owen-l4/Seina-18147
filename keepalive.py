from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return 'bot online'

def run():
    app.run()

def keep_alive():
    run()