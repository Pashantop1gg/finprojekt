import telebot
token="5439004926:AAFj7tHorcsWufuKESzgVhHXfl0YiAHZB28"
bot=telebot.TeleBot(5439004926:AAFj7tHorcsWufuKESzgVhHXfl0YiAHZB28)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.file_name zxc name)