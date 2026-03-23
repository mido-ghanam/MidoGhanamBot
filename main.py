import telebot, os, sys, sqlite3

midobot = telebot.TeleBot("7573060217:AAE3HnTcBAwQ1X5sPoKrGg6r2WwLHv2LPe4")
db = sqlite3.connect('midobot.db', check_same_thread=False)
cursor = db.cursor()

@midobot.message_handler(commands=['start'])
def start(message):
  msg = f"""Welcome [{message.from_user.first_name} {f'{message.from_user.last_name}' if message.from_user.last_name else ''}](tg://user?id={message.from_user.id}) to the Midobot!
  {message.from_user.id}"""
  midobot.reply_to(message, msg, parse_mode='Markdown')

@midobot.message_handler(commands=['restart'])
def restart(message):
  midobot.reply_to(message, "Restarting Midobot...")
  os.system("clear" if os.name == "posix" else "cls")
  print("Midobot is restarting...")
  os.execv(sys.executable, [sys.executable] + sys.argv)

@midobot.message_handler(commands=['stop'])
def stop(message):
  midobot.reply_to(message, "Stopping Midobot...")
  os.system("clear" if os.name == "posix" else "cls")
  print("Midobot is stopped.")
  midobot.stop_polling()

os.system("clear" if os.name == "posix" else "cls")
print("Midobot is running...")
midobot.infinity_polling()