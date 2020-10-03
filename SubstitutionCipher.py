def substitution_cipher(message):
    orgAlphabet = "abcdefghijklmnopqrstuvwxyz"
    subAlphabet = "yhkqgvxfoluapwmtzecjdbsnri"
    size = len(message)
    output = ""
    if size == 0:
        return
    elif size !=0:
        for i in range(size):
            idx = orgAlphabet.find(message[i])
            if idx is not None:
                output += subAlphabet[idx]
            else:
                output += message[i]
    return output