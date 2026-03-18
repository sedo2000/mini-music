import requests
from .config import BOT_TOKEN, DEVELOPER_ID

API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id, text, keyboard=None):
    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": keyboard
    }
    requests.post(f"{API}/sendMessage", json=data)


def handle_update(update):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        keyboard = {
            "inline_keyboard": [[
                {
                    "text": "🎵 Open Mini App",
                    "web_app": {"url": "https://your-domain.vercel.app"}
                }
            ]]
        }
        send_message(chat_id, "Welcome to Mini Music 🎧", keyboard)

    elif text == "/admin":
        if chat_id != DEVELOPER_ID:
            send_message(chat_id, "Unauthorized")
            return

        send_message(chat_id, "Admin Panel:\n1. Broadcast\n2. Stats\n3. Logs")
