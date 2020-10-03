# message = 'I love to code in python.'
message = input("Please type your message: ")
translated = ''

i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print("The cipher text is : ", translated)
