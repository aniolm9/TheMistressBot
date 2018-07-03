import commands
import logging
import os
import handlers
from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, CommandHandler

def logs():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

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

def getCineRipoll():
        num = ""
        url = "http://circuiturgellenc.com/bku/index.php/component/k2/item/61-cinema-comtal.html"
        os.system("curl -s -o cine.html " + url)
        p = open("cine.html")
        web = BeautifulSoup(p, "html.parser")
        while "<h1>404 Not Found</h1>" in str(web):
            if num == "":
                num = 1
                url = "http://circuiturgellenc.com/bku1/index.php/component/k2/item/61-cinema-comtal.html"
                os.system("curl -s -o cine.html " + url)
                p = open("cine.html")
                web = BeautifulSoup(p, "html.parser")
            else:
                num += 1
                url = "http://circuiturgellenc.com/bku" + str(num) + "/index.php/component/k2/item/61-cinema-comtal.html"
                os.system("curl -s -o cine.html " + url)
                p = open("cine.html")
                web = BeautifulSoup(p, "html.parser")

        num = ""
        resultat = web.findAll('img')
        for i in resultat:
            i = str(i)
            if "_L.jpg" in i:
                inici = i.index('src="') + 5
                final = i.index('"', inici)
                ruta = i[inici:final].replace("_L.jpg", "_XL.jpg")
                #print (ruta)
                os.system("wget -q http://circuiturgellenc.com%s -O cineripoll.jpg" % ruta)