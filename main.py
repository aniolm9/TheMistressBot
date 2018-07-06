import functions
from telegram.ext import Updater

def main():
    # Call the logs function to start logging.
    functions.logs()
    # Create the Updater and pass the bot token;
    TOKEN=open("TOKEN", "r").readline()
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # Call the function that contains the handlers for the commands.
    functions.handlersProcess(updater, dispatcher)

# Rock it
main()
