from flask import Flask, jsonify
from threading import Thread
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Telegram Auto-Forward Bot",
        "message": "Bot is running successfully!"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/ping')
def ping():
    return "pong", 200

def run_web_server(port=8080):
    """
    Start the Flask web server on the specified port
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    logger.info(f"Starting web server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

def start_server_in_background(port=8080):
    """
    Start the web server in a background thread
    """
    server_thread = Thread(target=run_web_server, args=(port,), daemon=True)
    server_thread.start()
    return server_thread
