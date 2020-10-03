def playfair_cipher(plain,key):
    def sqMatrix(size,elements):
        matrix = [[0 for x in range(size)] for y in range(size)]
        i = 0
        for y in range(size):
            for x in range(size):
                matrix[y][x] = elements[i]
                i +=1
        return matrix

    key = [k for k in key.lower()]
    for k in range(97,123):
        if chr(k) not in key and chr(k) != "j": #both i and j are considered same
            key.append(chr(k))
  
    playfair = sqMatrix(5,key)
    # print(playfair)

    plain = plain.replace(" ",'')
    if len(plain)%2 != 0:
        plain += 'x'
    plain = [(plain[a],plain[a+1]) for a in range(0, len(plain), 2)]
    encrypted = ''
  
    for a,b in plain:
        for y in range(5):
            for x in range(5):
                if a == playfair[y][x]:
                    a = [y,x]
                elif b == playfair[y][x]:
                    b = [y,x]
        if  a[0] == b[0]: #same row
            # print(a,'   ',b)
            a[1] = (a[1] + 1) % 5
            b[1] = (b[1] + 1) % 5
            a[1],b[1] = b[1], a[1]
        elif a[1] == b[1]: #same clmn
            a[0] = (a[0] + 1) % 5
            b[0] = (b[0] + 1) % 5
            # a[0], b[0] = b[0], a[0]
        
        encrypted += playfair[a[0]][b[1]] + playfair[b[0]][a[1]]
    return encrypted
