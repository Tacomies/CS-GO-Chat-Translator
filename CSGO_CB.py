from os.path import exists
from googletrans import Translator
from time import sleep
gt = Translator()


def output(lst):
    for message in lst:
        print(f"{message[0]:<17} : {message[1]}")

def toEn(lst):
    translated = []
    for message in lst:
        temp = message.split(" : ")
        if gt.detect(temp[1]).lang != "en":
            translated.append([temp[0], gt.translate(temp[1], dest="en").text])
    return translated

def read_chat(path):
    with open(path, "r") as log:
        return [line for line in log if " : " in line]

def clearLog(path): #Clearing log for better performance
    open(path, "w")

def main():
    config = {}
    with open("config.txt", "r") as conf:
        config["path"] = conf.read()
    clearLog(config["path"])
    
    while True:
        toTranslate = read_chat(config["path"])
        output(toEn(toTranslate))
        sleep(1)

def setup():
    with open("config.txt", "w") as config:
        config.write(input("Path to logfile: "))
        print("\nSaved!")
        main()

#Deciding if setup is necessary
if __name__ == "__main__":
    if exists("config.txt") == True:
        main()
    else:
        setup()
        
