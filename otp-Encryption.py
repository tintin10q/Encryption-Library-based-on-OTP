import string


class Encrypt:
    def __init__(self, message, key="none"):

        self.to_num_dict = {}
        self.to_str_dict = {}

        counter = 1
        for i in string.printable[:-5]:
            self.to_str_dict[counter] = i
            self.to_num_dict[i] = counter
            counter += 1

        self.IDs = len(self.to_str_dict)
        if key == "none":
            self.key = "".join([str(i) for i in self.to_number(message)])
        else:
            self.key = "".join([str(i) for i in self.to_number(key)])
        self.message = message
        self.key1 = self.key
        self.key = int(self.reverse(self.key1))  # Reverse key and turn it back into an integer
        # self.key = int(((self.key / 2 * 6) ** 4))  # Mess a bit with the key (disabled as this is not universal)
        self.key = self.list_to_int(str(self.key1))  # Turn it into a list
        self.message = self.to_number(self.message)  # Text input that get's changed to a list

    def encrypt(self):
        return "".join(self.to_text(self.calculate_plus(self.key, self.message)))

    def decrypt(self):
        return "".join(self.to_text(self.calculate_min(self.key, self.message)))

    def to_number(self, text_input):  # Convert chars to numbers in a list
        return [self.to_num_dict[x] for x in text_input]

    def to_text(self, number_input):  # Convert numbers to chars in a list
        return [self.to_str_dict[x] for x in number_input]

    @staticmethod
    def list_to_int(key):  # Turn the key into a list
        return [int(c) for c in key]

    @staticmethod
    def reverse(message):
        """ Reverses the input"""
        return str(message)[::-1]

    def calculate_plus(self, key, text):  # Encrypt is +
        point, point1 = 0, 0
        while point != len(text):
            text[point] += key[point1]
            if text[point] > self.IDs:
                text[point] -= self.IDs
            point += 1
            if point1 != (len(key) - 1):
                point1 += 1
            else:
                point1 = 0
        return text

    def calculate_min(self, key, text):  # Decrypt is -
        point, point1 = 0, 0
        while point != len(text):
            text[point] -= key[point1]
            if text[point] < 1:
                text[point] += self.IDs
            point += 1
            if point1 != (len(
                    key) - 1):
                point1 += 1
            else:
                point1 = 0
        return text


"""
# Encrypt Class 
print("abcde")
encrypted = Encrypt("abcde").encrypt()
decrypted = Encrypt(encrypted,"abcde").decrypt()
print(encrypted,decrypted)
"""
