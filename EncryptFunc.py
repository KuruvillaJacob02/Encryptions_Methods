# All the encryption methods must be added as a fucntion over here
# These functions will then be called in the main file
def atbash(string):
    s2=''
    for char in string:
        if char.islower()==True:
            s2+=chr(122-(ord(char)-97))
        elif char.isupper()==True:
            s2+=chr(90-(ord(char)-65))
        else:
            s2+=char
    string=s2
    return string
def caesar_cipher(s, k):
    s2=''
    for char in s:
        if char>='a' and char<='z':
            asciival=ord(char)+k
            if asciival>122:
                asciival=96+(asciival-122)
            s2+=chr(asciival)
        elif char>='A' and char<='Z':
            asciival=ord(char)+k
            if asciival>90:
                asciival=64+(asciival-90)
            s2+=chr(asciival)
        else:
            s2+=char
    s=s2
    return s
