from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running", 200

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
