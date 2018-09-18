#n => i + 0
#n => j + 1
#s => i - 0
#s => j - 1
#e => i + 1
#e => j + 0
#w => i - 1
#w => j - 0

#1,1 -> N
#1,2 -> S, N, E
#1,3 -> S, E
#2,1 -> N
#2,2 -> S, W
#2,3 -> W, E
#3,1 -> "Victory!"
#3,2 -> S, N
#3,3 -> S, W

#Þurfum að nota while svo hægt sé að fara fram og til baka án þess að skrifa 
#endalausann kóða.

#afþví við byrjum í 1,1
i = 1
j = 1


while j < 4:
    location = str(i) + str(j)
    if location == '11':
        print("You can travel: (N)orth.")
        direction = str(input("Direction: "))
        if direction in 'nN':
            j = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'nN':
                j = 2
            else:
                print("Not a valid direction!")
    elif location == '12':
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = str(input("Direction: "))
        if direction in 'nN':
            j = 3 
        elif direction in 'sS':
            j = 1
        elif direction in 'eE':
            i = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'nN':
                j = 3 
            elif direction in 'sS':
                j = 1
            elif direction in 'eE':
                i = 2
            else:
                print("Not a valid direction!")
    elif location == '13':
        print("You can travel: (E)ast or (S)outh.")
        direction = str(input("Direction: "))
        if direction in 'eE':
            i = 2
        elif direction in 'sS':
            j = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'eE':
                i = 2
            elif direction in 'sS':
                j = 2
            else:
                print("Not a valid direction!")
    elif location == '21':
        print("You can travel: (N)orth.")
        direction = str(input("Direction: "))
        if direction in 'nN':
            j = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'nN':
                j = 2
            else:
                print("Not a valid direction!")
    elif location == '22':
        print("You can travel: (S)outh or (W)est.")
        direction = str(input("Direction: "))
        if direction in 'sS':
            j = 1
        elif direction in 'wW':
            i = 1
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'sS':
                j = 1
            elif direction in 'wW':
                i = 1
            else:
                print("Not a valid direction!")
    elif location == '23':
        print("You can travel: (E)ast or (W)est.")
        direction = str(input("Direction: "))
        if direction in 'eE':
            i = 3
        elif direction in 'wW':
            i = 1
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'eE':
                i = 3
            elif direction in 'wW':
                i = 1
            else:
                print("Not a valid direction!")
    elif location == '33':
        print("You can travel: (S)outh or (W)est.")
        direction = str(input("Direction: "))
        if direction in 'sS':
            j = 2
        elif direction in 'wW':
            i = 2
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'sS':
                j = 2
            elif direction in 'wW':
                i = 2
            else:
                print("Not a valid direction!")
    elif location == '32':
        print("You can travel: (N)orth or (S)outh.")
        direction = str(input("Direction: "))
        if direction in 'sS':
                j = 1
        elif direction in 'nN':
                j = 3
        else:
            print("Not a valid direction!")
            direction = str(input("Direction: "))
            if direction in 'sS':
                j = 1
            elif direction in 'nN':
                j = 3
            else:
                print("Not a valid direction!")
    else:
        print('Victory!')
        j = 5
        i = 5