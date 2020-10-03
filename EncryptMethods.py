from EncryptFunc import *
ch=1
while ch!=0:
    print("(1)Ceasar's Cipher")      #Do not forget to add the encryption method option
    print("(2)Atbash Cipher")        # in the menu
    print("(0)Exit Menu")
    ch=int(input("Enter Encryption choice (1/2/0)")) #Also update the choices here
    if ch==1:
        print("Code yet to be Implemented")
    elif ch==2:
        string=input("Enter String")
        string=atbash(string)
        print(string)
       