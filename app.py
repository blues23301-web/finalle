from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder=".")

BOT_TOKEN = os.getenv("https://api.telegram.org/bot{BOT_TOKEN}/sendMessage")
CHAT_ID = os.getenv("8994413452")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

@app.route("/script.js")
def js():
    return send_from_directory(".", "script.js")

@app.route("/apply", methods=["POST"])
def apply():

    data = request.get_json()

    fullname = data.get("fullname", "")
    phone = data.get("phone", "")
    amount = data.get("amount", "")
    period = data.get("period", "")
    country = data.get("country", "")

    message = f"""
NEW LOAN APPLICATION

Name: {fullname}
Phone: {phone}
Amount: {amount}
Repayment Period: {period}
Country: {country}
"""

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        telegram_url,
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    if response.status_code == 200:
        return jsonify({"success": True})

    return jsonify({"success": False}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
