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
north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '
i = 1
j = 1
valid = ''
text = ''
def valid_input(valid,location,text):
    if location == '11':
        text = travel + north + '.'
        valid = 'nN'
        return valid,text

    elif location == '12':
        text = travel + north + ' or ' + east + ' or ' + south + '.'
        valid = 'nNeEsS'
        return valid,text

    elif location == '13':
        text = travel + east + ' or ' + south + '.'
        valid = 'eEsS'
        return valid,text

    elif location == '21':
        text = travel + north + '.'
        valid = 'nN'
        return valid,text

    elif location == '22':
        text = travel + south + ' or ' + west + '.'
        valid = 'sSwW'
        return valid,text

    elif location == '23':
        text = travel + east + ' or ' + west + '.'
        valid = 'eEwW'
        return valid,text

    elif location == '33':
        text = travel + south + ' or ' + west + '.'
        valid = 'SswW'
        return valid,text

    elif location == '32':
        text = travel + north + ' or ' + south + '.'
        valid = 'nNSs'
        return valid,text

    else:
        text = 'Victory!'
        valid = ''
        return valid,text

def find_direction(valid,i,j):
    while True:
        direction = str(input("Direction: "))
        if direction in valid:
            if direction in 'sS':
                j -= 1
                return i,j
            elif direction in 'nN':
                j += 1
                return i,j
            elif direction in 'wW':
                i -= 1
                return i,j
            else:
                i += 1
                return i,j
        else:
            print("Not a valid direction!")

while i < 4:
    while j < 4:
        location = str(i) + str(j)

        valid, text = valid_input(valid,location,text)
        print(text)

        if text == 'Victory!':
            i = 5
            j = 5

        else:
            i, j = find_direction(valid,i,j)