import random

class RBCipher(object):
    """
    This class implements a running-key book cipher. This makes use of any text file stored
    as plain text in ./resources. By default, this is "A Tale of Two Cities" by Charles Dickens.
    The encrypt method goes to a random location, k, and uses letters from that point onwards as
    a key, which is then used to encrypt the message by modulo addition.
    
    Like all book-based ciphers, it is fast, practical, and can be done without a computer, although
    it is not safe against advanced crytanalysis due to the non-random nature of natural language.
    
    Only some punctuation is allowed. This reduces the size of available characters, increasing
    the entropy and so the security. Characters not in self.goodchars will be omitted.

    The encrypted message is of the form k-xxxxx where k is the start location in the keytext.
    """

    def __init__(self, book_file='TOTC.txt'):
        with open('./resources/{}'.format(book_file), 'r') as file: 
            self.keytext = file.read()

        # Make sure that space is always included in self.allowed_punctuation.
        self.allowed_punctuation = ' ,.#'
        self.goodchars = 'qwertyuiopasdfghjklzxcvbnm1234567890' + self.allowed_punctuation
        self.N = len(self.goodchars)

    def encrypt(self, strin):
        message_str = self.increase_entropy(strin)
        random.seed(1)
        start_location = random.randint(0,len(self.keytext)-len(message_str)-1)
        encrypted_str = self.translate(message_str, start_location, 'encrypt')
        return str(start_location) + '-' + encrypted_str

    def decrypt(self, strin):
        try:
            start_location, encrypted_str = strin.split('-',1)
        except:
            breakpoint()
        start_location = int(start_location)
        message_str = self.translate(encrypted_str, start_location, 'decrypt')
        return message_str

    def translate(self, input_str, start_location, mode='encrypt'):
        """
        General-purpose function for both encryption and decryption.
        """
        key_str = self.get_key_interval(start_location, len(input_str))
        input_int = [self.ord_safe(c) for c in input_str]
        key_int     = [self.ord_safe(c) for c in key_str]

        if mode=='encrypt':
            output_int = [(input_int[i]+key_int[i])%self.N for i in range(len(key_str))]
        elif mode=='decrypt':
            output_int = [(input_int[i]-key_int[i])%self.N for i in range(len(key_str))]
        output_str = ''.join([self.chr_safe(n) for n in output_int])

        return output_str

    def ord_safe(self, char):
        """
        A function which is like the built-in ord(), but mapping to a continuous range of
        numbers to allow for modulo addition.
        """
        assert type(char)==str and len(char)==1 and char.lower()==char
        if char.isnumeric():
            num = ord(char)-48
        elif char.isalpha():
            num = ord(char)-87
        elif char in self.allowed_punctuation:
            num = self.allowed_punctuation.index(char)+36
        else:
            print(char)
            raise NotImplementedError
        return num

    def chr_safe(self, num):
        """
        The inverse of ord_safe.
        """
        assert type(num)==int and num>=0
        if num<=9:
            char = str(num)
        elif num<=35:
            char = chr(num+87)
        elif num<=35+len(self.allowed_punctuation):
            char = self.allowed_punctuation[num-36]
        else:
            print(num)
            raise NotImplementedError
        if char=='{':
            breakpoint()
        return char

    def get_key_interval(self, start, length):
        """
        This gets a key comprising only of character in self.goodchars of the same length
        as the input message.
        """
        cursor = start+length
        key = self.keytext[start:cursor]
        key = self.increase_entropy(key)
        while len(key)<length:
            cursor_end = cursor + int(length/2)
            new_part = self.keytext[cursor:cursor_end]
            key = key + self.increase_entropy(new_part)
            cursor = cursor_end
        return key[:length]

    def increase_entropy(self, strin):
        """
        Here we reduce the number of characters that can be present in the message. 
        Since the key text comprises mostly english characters, any characters outside
        of this will reduce the entropy and so the security of the cipher. 
        For the same reason, the decrypted message is always in lower-case.
        """
        strin = strin.lower()
        for c in set(strin):
            if c not in self.goodchars:
                strin = strin.replace(c, '')
        return strin









































