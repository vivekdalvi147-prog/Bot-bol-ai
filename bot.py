import os
import telebot
import requests

# Token ko environment variable se lega (security ke liye)
BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_API_URL = "https://bol-ai.vercel.app/api/chat"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running on Cloud!")

@bot.message_handler(func=lambda message: True)
def chat(message):
    payload = {"messages": [{"role": "user", "content": message.text}]}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(AI_API_URL, json=payload, headers=headers)
        bot.reply_to(message, response.text.strip())
    except:
        bot.reply_to(message, "Error connecting to AI.")

# Is line se bot chalu hota hai
if __name__ == "__main__":
    bot.infinity_polling()
