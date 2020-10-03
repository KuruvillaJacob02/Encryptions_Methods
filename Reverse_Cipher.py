# message = 'I love to code in python.'
def Reverse_cipher(message):
   translated = ''
   i = len(message) - 1
      while i >= 0:
         translated = translated + message[i]
         i = i - 1
      s = "The cipher text is : "+translated
   return s

