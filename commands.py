import os
import random
import functions

def start(bot, update):
    bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/welcome.ogg', 'rb'))

def stop(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open('imatges/DioStop.jpg', 'rb'))

def allonsy(bot, update):
    bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/allons-y.ogg', 'rb'))

def geronimo(bot, update):
    bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/geronimo.ogg', 'rb'))

def ohmygod(bot, update):
    bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/ohmygod.ogg', 'rb'))

def zawarudo(bot, update):
    bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/zawarudo.ogg', 'rb'))

def stayout(bot, update):
    bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/stayout.ogg', 'rb'))

def gtfo(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open('imatges/gtfo.jpg', 'rb'))

def btfo(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open('imatges/btfo.jpg', 'rb'))

def stfu(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open('imatges/stfu.jpg', 'rb'))

def flowchart(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=open('imatges/flowchart.jpg', 'rb'))

def random_command(bot, update, args):
    files = functions.memes()
    try:
        ordre = args[0]
        if (ordre == "total"):
            bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="El nombre actual de mems és de " + str(len(files)) + ".")
    except:

        ran = random.choice(os.listdir("memes"))
        for (n, i) in enumerate(files):
            if (i == ran):
                f = open("memes/" + ran, "rb")
                bot.send_photo(chat_id=update.message.chat_id, photo=f, caption=n+1, reply_to_message_id=update.message.message_id)
                break

def cineripoll(bot, update):
    functions.getCineRipoll()
    bot.send_photo(chat_id=update.message.chat_id, photo=open("cineripoll.jpg", 'rb'), reply_to_message_id=update.message.message_id)

def meme(bot, update, args):
    files = functions.memes()
    try:
        num = int(args[0])
        if (num < 1 or num > len(files)):
            bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="Aquest valor no és vàlid!")
        else:
            f = open("memes/" + files[num - 1], "rb")
            bot.send_photo(chat_id=update.message.chat_id, photo=f, reply_to_message_id=update.message.message_id)
    except:
        bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="M'has de passar un nombre natural diferent de 0!")
