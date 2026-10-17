import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

@app.route("/")
def home():
    return "KODEX MEDIA GROUP server is running!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or {}

    if not BOT_TOKEN or not CHAT_ID:
        return jsonify({
            "ok": False,
            "error": "Server configuration is incomplete"
        }), 500

    text = (
        "💜 НОВАЯ ЗАЯВКА — KODEX MEDIA GROUP\n\n"
        f"👤 Имя: {data.get('name', '—')}\n"
        f"🏢 Проект: {data.get('project', '—')}\n"
        f"🛠 Услуга: {data.get('service', '—')}\n"
        f"📝 Задача: {data.get('task', '—')}\n"
        f"💰 Бюджет: {data.get('budget', '—')}\n"
        f"📅 Срок: {data.get('deadline', '—')}\n"
        f"📞 Контакт: {data.get('contact', '—')}"
    )

    try:
        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text},
            timeout=20
        )
        response.raise_for_status()
        result = response.json()

        if not result.get("ok"):
            return jsonify({"ok": False}), 502

        return jsonify({"ok": True})

    except requests.RequestException:
        app.logger.exception("Telegram sendMessage failed")
        return jsonify({"ok": False}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
