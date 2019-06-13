import commands
import logging
import os
import handlers
import datetime
import jobs
from telegram.ext import MessageHandler, CommandHandler

def logs():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def jobsManager(jobsqueue):
    # Cine Ripoll job. Every Thursday at 08:30 download the schedule.
    today = datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day, 8, 30, 0)
    next_thursday = today + datetime.timedelta(days=(3-today.weekday())%7)
    jobsqueue.run_repeating(jobs.getCineRipoll, interval=next_thursday)

def handlersProcess(updater, dispatcher):
    # Dictionary containing all the command handlers
    handlers_dict = dict(start=CommandHandler('start', commands.start),
                         stop=CommandHandler('stop', commands.stop),
                         allonsy=CommandHandler('allonsy', commands.allonsy),
                         geronimo=CommandHandler('geronimo', commands.geronimo),
                         ohmygod=CommandHandler('ohmygod', commands.ohmygod),
                         zawarudo=CommandHandler('zawarudo', commands.zawarudo),
                         stayout=CommandHandler('stayout', commands.stayout),
                         gtfo=CommandHandler('gtfo', commands.gtfo),
                         btfo=CommandHandler('btfo', commands.btfo),
                         stfu=CommandHandler('stfu', commands.stfu),
                         flowchart=CommandHandler('flowchart', commands.flowchart),
                         random=CommandHandler('random', commands.random_command, pass_args=True),
                         cineripoll=CommandHandler('cineripoll', commands.cineripoll),
                         meme=CommandHandler('meme', commands.meme, pass_args=True))

    # Adding handlers to dictionary
    #handlers_dict["start"] = CommandHandler('start', commands.start)

    # Adding the handlers to the dispatcher.
    for command in handlers_dict:
        dispatcher.add_handler(handlers_dict[command])

    # Error handler
    dispatcher.add_error_handler(handlers.error)

    # Entry and exit handler
    dispatcher.add_handler(MessageHandler(None, handlers.entryAndExit))

    # Start the bot
    updater.start_polling()

    # Wait for Ctrl-C or other SIGs to end the process
    updater.idle()

# Function that returns the list of memes
def memes():
    files = os.listdir("memes")
    files.sort(key=lambda x: os.stat(os.path.join("memes", x)).st_mtime)
    return files
