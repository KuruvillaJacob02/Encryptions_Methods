from Ceasarscipher import caesar_cipher
from AbtashCipher import atbash
from ColumnarTranspositionCipher import transpositionCipher
from PlayfairCipher import playfair_cipher
from RunningBookCipher import RBCipher

ch=1
while ch!=0:
    print("(1) Ceasar's Cipher")      #Do not forget to add the encryption method option
    print("(2) Atbash Cipher")        # in the menu
    print("(3) ColumnarTranspositionCipher")
    print("(4) Playfair Cipher")
    print("(5) Reverse Cipher")
    print("(6) Running-Key Book Cipher")
    print("(0) Exit Menu")
    ch = int(input("Enter Encryption choice (1/2/3/4/5/6/0): ")) #Also update the choices here
    if ch==1:
        s=input("Enter String: ")
        k=int(input("Enter the shift value: "))
        s=caesar_cipher(s, k)
        print(s)
    
    elif ch==2:
        string=input("Enter String: ")
        string=atbash(string)
        print(string)

    elif ch==3:
        message = input("Enter Message: ")
        key = int(input("Enter key: "))
        message = transpositionCipher(key,message) 
        print(message) 
        
    elif ch == 4:
        string = input("Enter string:")
        key = input("Enter the key (a string):")
        print(playfair_cipher(string,key))
        
    elif ch==5:
        message = input("Enter your message: ")
        print(Reverse_cipher(message))
        
    elif ch==6:
        crypter = RBCipher()
        mode = input('Encrypt [e] or decrypt [d]? ')

        if mode.lower()=='e':
            message = input("Enter Message: ")
            out = crypter.encrypt(message)
            print('Encrypted message:', out, '\n')

        elif mode.lower()=='d':
            enc = input("Enter encrypted message: ")
            out = crypter.decrypt(enc)
            print('Message:', out, '\n')

        else:
            print('Mode not recognised')
    

