import os
import threading
from dotenv import load_dotenv
import telebot
from flask import Flask

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Telegram bot handlers
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id ,text="Hi! I'm Iscreamy, your helpful to-do list assistant. How can I help?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot in a separate thread
def start_bot():
    bot.infinity_polling()

print("Running bot...")
bot.infinity_polling()
#threading.Thread(target=start_bot).start()

'''# Dummy web server to keep Render alive
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render provides PORT
    app.run(host='0.0.0.0', port=port)
'''