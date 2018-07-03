import functions

def error(update, error):
    logger = functions.logs()
    logger.warning('Update "%s" caused error "%s"', update, error)

def entryAndExit(bot, update):
    if (len(update.message.new_chat_members) > 0):
        bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/welcome.ogg', 'rb'))
    if (update.message.left_chat_member != None):
        bot.send_audio(chat_id=update.message.chat_id, audio=open('sons/stayout.ogg', 'rb'))