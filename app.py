from flask import Flask, jsonify, request
import threading
import requests
import time
import os
import json

# Define the Flask app instance
app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"status": "alive"})


# New endpoint to call external APIs
@app.route("/call_api", methods=["POST"])
def call_api():
    data = request.get_json()
    url = data.get("url")
    method = data.get("method", "GET").upper()
    payload = data.get("payload", {})
    headers = data.get("headers", {})
    try:
        resp = requests.request(method, url, json=payload, headers=headers)
        return jsonify({
            "status": "success",
            "code": resp.status_code,
            "headers": dict(resp.headers),
            "body": resp.json() if 'application/json' in resp.headers.get('Content-Type', '') else resp.text
        })
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500


def self_ping():
    # Hardcoded list of URLs to ping
    # Hardcoded list of URLs to ping
    url_list = [
        "https://web-caller-pik3.onrender.com/ping",
        "https://war-backend-e8v5.onrender.com/"
        # Add more URLs here as needed
        # "https://example.com/another-api"
    ]
    while True:
        for url in url_list:
            try:
                requests.get(url)
            except Exception as e:
                print(f"Self-ping error for {url}: {e}")
        time.sleep(3)

if __name__ == "__main__":
    # Start self-ping in a background thread
    threading.Thread(target=self_ping, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
