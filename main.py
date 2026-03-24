from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot, os, sys
from . import utils

midobot = telebot.TeleBot("7573060217:AAE3HnTcBAwQ1X5sPoKrGg6r2WwLHv2LPe4")

@midobot.message_handler(commands=['start'])
def start(message):
  msg = f"Welcome [{message.from_user.first_name} {f'{message.from_user.last_name}' if message.from_user.last_name else ''}](tg://user?id={message.from_user.id}) to the Midobot!"
  buttons = InlineKeyboardMarkup()
  buttons.add(InlineKeyboardButton("Projects", callback_data="projects"), InlineKeyboardButton("Skills", callback_data="skills"))
  buttons.add(InlineKeyboardButton("Contact", callback_data="contact"), InlineKeyboardButton("About Me", callback_data="about"))
  buttons.add(InlineKeyboardButton("Buy me a coffee", callback_data="coffee"))
  midobot.reply_to(message, msg, parse_mode='Markdown', reply_markup=buttons)

@midobot.callback_query_handler(func=lambda call: call.data == "projects")
def projects_callback(call):
  midobot.edit_message_text("Please wait while collecting data from server..", call.message.chat.id, call.message.message_id)
  msg = f"{utils.projects.get_projects_count()} Project Has been completed.."
  midobot.edit_message_text(msg, call.message.chat.id, call.message.message_id)



@midobot.callback_query_handler(func=lambda call: call.data == "skills")
def skills_callback(call):
  midobot.edit_message_text("Please wait while collecting data from server..", call.message.chat.id, call.message.message_id)

@midobot.callback_query_handler(func=lambda call: call.data == "contact")
def contact_callback(call):
  midobot.edit_message_text("Please wait while collecting data from server..", call.message.chat.id, call.message.message_id)

@midobot.callback_query_handler(func=lambda call: call.data == "about")
def about_callback(call):
  midobot.edit_message_text("Please wait while collecting data from server..", call.message.chat.id, call.message.message_id)

@midobot.callback_query_handler(func=lambda call: call.data == "coffee")
def coffee_callback(call):
  midobot.edit_message_text("Please wait while collecting data from server..", call.message.chat.id, call.message.message_id)


@midobot.message_handler(commands=['restart'])
def restart(message):
  midobot.reply_to(message, "Restarting Midobot...")
  os.system("clear" if os.name == "posix" else "cls")
  print("Midobot is restarting...")
  os.execv(sys.executable, [sys.executable, "-m", "MidoGhanamBot.main"])

@midobot.message_handler(commands=['stop'])
def stop(message):
  midobot.reply_to(message, "Stopping Midobot...")
  os.system("clear" if os.name == "posix" else "cls")
  print("Midobot is stopped.")
  midobot.stop_polling()

os.system("clear" if os.name == "posix" else "cls")
print("Midobot is running...")
midobot.infinity_polling()