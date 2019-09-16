from flask import Flask, render_template, redirect, url_for, request
from string import printable
''''
Dit programma verseutelt text met een sleutel. Je kan de text alleen maar terug krijgen als je de juiste sleutel geeft.
Door Quinten Cabo
'''

app = Flask(__name__)
from pprint import pprint
class Encrypt():
    def __init__(self, key, message,power=1):
        # dit zijn de input handeler woordenboeken
        character_id = 1
        self.to_num_dict = {}
        self.to_str_dict = {}
        # generate dicts
        for character in printable[:-5].replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ",""):
            self.to_num_dict[character] = character_id
            self.to_str_dict[character_id] = character
            character_id += 1
        pprint(self.to_str_dict)
        pprint(self.to_num_dict)
        self.IDs = len(self.to_str_dict)
        self.key = key
        self.power = power
        self.message = message
        self.message_backup = message
        self.key = int(self.reverse(key))  # voer de reverse uit op key en maak er een int van
        # self.key = int(((self.key / 2 * 6) ** 4))  # berekening voor exstra bevijliging
        print(self.key)
        self.key = self.list_to_int(str(key))  # omzetten naar list
        print(self.key)
        self.message = self.tonum(self.message.lower())  # text input die gelijk naar een lijst gezet wordt

    def encrypt(self):
        if self.power <= 0:
            return self.message_backup+"\n powerlevel 0 or less does nothing"
        else:
            for i in range(0,self.power):
                self.output = "".join(self.totext(self.calculateplus(self.key, self.message)))
        return self.output

    def decrypt(self):
        if self.power <= 0:
            return self.message_backup+"\n powerlevel 0 or less does nothing"
        else:
            for i in range(0,self.power):
                self.output = "".join(self.totext(self.calculatemin(self.key, self.message)))
        return self.output

    def tonum(self, input):  # zet de text str om in int en in een lijst
        return [self.to_num_dict[x] for x in input]

    def totext(self, input):  # zet de text int om naar str in lijst
        return [self.to_str_dict[x] for x in input]

    def list_to_int(self, key):  # zet de key in een lijst
        return [int(c) for c in key]

    def reverse(self, message):  # keert de key om voor exstra berekenheid
        c = len(message) - 1
        return ''.join([str(i) for i in range(c, -1, -1)])

    def calculateplus(self, key, text):  # encrypt dus +
        point, point1 = 0, 0
        while point != len(text):
            print(text[point],key[point1])
            text[point] += key[point1]
            if text[point] > self.IDs:
                text[point] -= self.IDs
            point += 1
            if point1 != (len(
                    key) - 1):  # die -1 is omdat een lijst met 0 begint en de len bij 1 begint hierdoor wordt point1 te laat tot 0 gereset
                point1 += 1
            else:
                point1 = 0
        return text

    def calculatemin(self, key, text):  # decrypt dus min
        point, point1 = 0, 0
        while point != len(text):
            print(text[point], key[point1])
            text[point] -= key[point1]
            if text[point] < 1:
                text[point] += self.IDs
            point += 1
            if point1 != (len(
                    key) - 1):  # die -1 is omdat een lijst met 0 begint en de len bij 1 begint hierdoor wordt point1 te laat tot 0 gereset
                point1 += 1
            else:
                point1 = 0
        return text

# Call as print(Encrypt("1221","hi").encrypt())
# Call as print(Encrypt("1221","ik").decrypt())


@app.route("/encryption/",methods=["POST","GET"])
def encrypt_decrypt():
    if request.method == "POST":
        e_or_d = request.form["e_or_d"]
        input_string = request.form["input_string"]
        key = request.form["key"]
        power = int(request.form["power"])
        if power >= 101:
            power = 100
        if e_or_d == "encrypt":
            return_string = Encrypt(key,input_string,power).encrypt()
        if e_or_d == "decrypt":
            return_string = Encrypt(key,input_string,power).decrypt()
        return render_template("encryption.html",finish=return_string,last_power=power,key=key,old_input=input_string)
    else:
        return render_template("encryption.html")

@app.route("/")
def home():
    return redirect(url_for("encrypt_decrypt"))
if __name__ == "__main__":
    app.run(debug=True)
