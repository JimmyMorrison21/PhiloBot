import os

import telebot
from Creator import create_joke as cj
from Text import get_text

token = '*********************'

bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['Hello'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую тебя")


@bot.message_handler(content_types=['photo'])
def send_text(message):
    print
    'message.photo =', message.photo
    fileID = message.photo[-1].file_id
    print
    'fileID =', fileID
    file_info = bot.get_file(fileID)
    print
    'file.file_path =', file_info.file_path
    downloaded_file = bot.download_file(file_info.file_path)
    with open("downloaded_image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    print(message)
    joke_text = get_text()
    cj(template="downloaded_image.jpg", joke_text=joke_text)
    os.remove('downloaded_image.jpg')
    with open("joke_image.png", 'rb') as filetosend:
        bot.send_photo(message.chat.id, filetosend)
    os.remove('joke_image.png')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
