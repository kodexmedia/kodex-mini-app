
import os
import requests
from flask import Flask, request

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
APP_URL = "https://kodexmedia.github.io/kodex-mini-app/"

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "KODEX Telegram bot is running!"


@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(silent=True) or {}
    message = update.get("message", {})

    if not message:
        return {"ok": True}

    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if text.startswith("/start") and chat_id:
        keyboard = {
            "inline_keyboard": [[
                {
                    "text": "📝 Оставить заявку",
                    "web_app": {"url": APP_URL}
                }
            ]]
        }

        welcome = (
            "🤖 Здравствуйте! Добро пожаловать в KODEX MEDIA GROUP!\n\n"
            "Мы превращаем идеи в цифровые решения с помощью "
            "искусственного интеллекта и современных технологий.\n\n"
            "🎬 AI-видео\n"
            "🧠 Нейросети\n"
            "🚀 Цифровые технологии\n\n"
            "📝 Нажмите кнопку ниже, чтобы оставить заявку.\n\n"
            "KODEX MEDIA GROUP | Ваши идеи, наши технологии."
        )

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": welcome,
                "reply_markup": keyboard
            },
            timeout=20
        )

    return {"ok": True}


if __name__ == "__main__":
    if BOT_TOKEN:
        webhook_url = "https://kodex-telegram-bot.onrender.com/webhook"
        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
            json={"url": webhook_url},
            timeout=20
        )
        print("Webhook setup:", response.text)

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
