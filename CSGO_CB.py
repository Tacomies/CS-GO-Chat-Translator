from os.path import exists
from googletrans import Translator
from time import sleep
gt = Translator()


def output(lst): #Prints messages nicely formatted
    for message in lst:
        print(f"{message[0].replace('(Terrorist) ', '').replace('(Counter-Terrorist) ', ''):<17} : {message[1]}")

def toEn(lst): #Translates messages to English
    translated = []
    for message in lst:
        temp = message.split(" : ")
        if gt.detect(temp[1]).lang != "en":
            translated.append([temp[0], gt.translate(temp[1], dest="en").text])
    return translated

def read_chat(path): #Reads logfile
    with open(path, encoding = 'utf-8', mode = 'r') as log:
        return [line for line in log if " : " in line]

def clearLog(path): #Clearing log for better performance
    open(path, "w")

def main(): #main Program
    config = {}
    with open("config.txt", encoding = 'utf-8', mode = 'r') as conf:
        config["path"] = conf.read() 
    while True:
        toTranslate = read_chat(config["path"])
        messages = toEn(toTranslate)
        output(messages)
        clearLog(config["path"])
        sleep(1)

def setup(): #Setup if you don't have set configs
    with open("config.txt", encoding = 'utf-8', mode = 'w') as config:
        path = input("Path to logfile: ")
        config.write(path)
    print("\nSaved!")
    main()

def start(): #Deciding starting method
    if exists("config.txt"):
        main()
    else:
        setup()


if __name__ == "__main__":
    start()
        
