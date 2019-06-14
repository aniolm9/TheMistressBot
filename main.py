import sys
import functions
from telegram.ext import Updater
try:
    from settings_secret import *
except:
    sys.exit("Missing settings_secret.py file.")

def main():
    # Call the logs function to start logging.
    functions.logs()

    # Create the Updater and pass the bot token.
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    jobqueue = updater.job_queue

    # Call the function that controls the jobs.
    functions.jobsManager(jobqueue)

    # Call the function that contains the handlers for the commands.
    functions.handlersProcess(updater, dispatcher)

# Rock it
main()
