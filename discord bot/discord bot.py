import discord
from discord.ext import commands
import asyncio
import os
import sys

''''
Dit programma verseutelt text met een sleutel. Je kan de text alleen maar terug krijgen als je de juiste sleutel geeft.
Door Quinten Cabo
'''


class Crypt():
    def __init__(self, key, *args):
        # dit zijn de input handeler woordenboeken
        self.to_num_dict = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,
                            "l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,
                            "v":22,"w":23,"x":24,"y":25,"z":26," ":27,".":28,",":29,"!":30,"?":31,
                            ")":32,"(":33,":":34,"'":35,"-":36,"_":37,"/":38,":":39,"=":40,"&":41,
                            "0":42,"1":43,"2":44,"3":45,"4":46,"5":47,"6":48,"7":49,"8":50,"9":51}

        self.to_str_dict = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",
                            12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",
                            22:"v",23:"w",24:"x",25:"y",26:"z",27:" ",28:".",29:",",30:"!",31:"?",
                            32:")",33:"(",34:":",35:"'",36:"-",37:"_",38:"/",39:":",40:"=",41:"&",
                            42:"0",43:"1",44:"2",45:"3",46:"4",47:"5",48:"6",49:"7",50:"8",51:"9"}
        self.IDs = len(self.to_str_dict)
        self.key = key
        self.message = "".join([str(i + " ") for i in args])  # I am adding spaces here and turning the args in to a single string
        self.message = self.message[:len(self.message) - 1]  # Removing the last added space
        self.key = int(self.reverse(self.key))  # voer de reverse uit op key en maak er een int van
        self.key = int((((self.key+70)/2*6)**4))  # berekening voor exstra bevijliging
        self.key = self.list_to_int(str(self.key))  # omzetten naar list
        self.message = self.tonum(self.message.lower())  # text input die gelijk naar een lijst gezet wordt

    def encrypt(self):
        self.output = "".join(self.totext(self.calculateplus(self.key, self.message)))
        return self.output

    def decrypt(self):
        self.output = "".join(self.totext(self.calculatemin(self.key, self.message)))
        return self.output

    def tonum(self, inputIn):  # zet de text str om in int en in een lijst
        return [self.to_num_dict[x] for x in inputIn]

    def totext(self, inputIn):  # zet de text int om naar str in lijst
        return [self.to_str_dict[x] for x in inputIn]

    def list_to_int(self, keyIn):  # zet de key in een lijst
        return [int(c) for c in keyIn]

    def reverse(self, message):  # keert de key om voor exstra berekenheid
        return message[::-1]

    def calculateplus(self, key, text):  # encrypt dus +
        point, point1 = 0, 0
        while point != len(text):
            text[point] += key[point1]
            if text[point] > self.IDs:
                text[point] -= self.IDs
            point += 1
            if point1 != (len(key)-1):  # die -1 is omdat een lijst met 0 begint en de len bij 1 begint hierdoor wordt point1 te laat tot 0 gereset
                point1 += 1
            else:
                point1 = 0
        return text

    def calculatemin(self, key, text):  # decrypt dus min
        point, point1 = 0, 0
        while point != len(text):
            text[point] -= key[point1]
            if text[point] < 1:
                text[point] += self.IDs
            point += 1
            if point1 != (len(key)-1):  # die -1 is omdat een lijst met 0 begint en de len bij 1 begint hierdoor wordt point1 te laat tot 0 gereset
                point1 += 1
            else:
                point1 = 0
        return text


# Call as print(Crypt("1221","hi").encrypt())
# Call as print(Crypt("1221","ik").decrypt())


description = 'yo'
bot = commands.Bot(command_prefix='>', description=description)

# Print the starting text
print("Starting up...")


@bot.event
async def on_ready():
    print('Encryption is ready for use')
    print('Name: {}'.format(bot.user.name))
    print('ID: {}\n~~~~~~~~~~'.format(bot.user.id))


helpsting = ">kill --> Used to shut down bot\n>ping --> Makes the bot return a message\n>encrypt <Key> <message> --> Uses the bot to encrypt a message\n>decrypt <Key> <message> 	--> Uses the bot to decrypt a message\n"


@bot.command()
async def help_me():
    await bot.say(helpsting)


@bot.command()
async def kill():
    await bot.say("Shutting down...")
    await bot.close()


@bot.command()
async def encrypt(message,key: str, *args: str):
    print(key,"".join([str(i + " ") for i in args]))
    messageOut = Crypt(key, *args).encrypt()
    await bot.say(messageOut)


@bot.command()
async def decrypt(key: str, *args: str):
    messageOut = Crypt(key, *args).decrypt()
    print(key,messageOut)
    await bot.say(messageOut)


@bot.command()
async def ping():
    await bot.say('Pong!')

import json
try:
    open('discord-bot-key.json')
    bot.run(key)
except FileNotFoundError:
    print("'discord-bot-key.json' not found!")
    input("\nPress enter to exit")
