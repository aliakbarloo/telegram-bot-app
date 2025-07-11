import telebot

BOT_TOKEN = "توکن_ربات_تو_اینجا"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام علی جان! 🌸 ربات روشنه.")

bot.polling()
