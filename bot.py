import telebot
from handlers import handle_start, handle_message, handle_check, handle_stats
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    handle_start(bot, message)

@bot.message_handler(commands=['done'])
def done_command(message):
    handle_check(bot, message)

@bot.message_handler(commands=['stats'])
def stats_command(message):
    handle_stats(bot, message)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    handle_message(bot, message)

if __name__ == '__main__':
    bot.polling()
