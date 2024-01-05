from collections import deque

password = deque('fbgdceah')

for cc in [a.strip().split() for a in open('day-21.input', 'r').readlines()][::-1]:
    if cc[0] == 'swap':
        if cc[1] == 'position':
            x = int(cc[2])
            y = int(cc[-1])
            password[x], password[y] = password[y], password[x]
        elif cc[1] == 'letter':
            x = cc[2]
            y = cc[-1]
            for i, c in enumerate(password):
                if c == x:
                    password[i] = y
                elif c == y:
                    password[i] = x
    elif cc[0] == 'rotate':
        if cc[1] == 'left':
            password.rotate(int(cc[2]))
        elif cc[1] == 'right':
            password.rotate(-int(cc[2]))
        elif cc[1] == 'based':
            r = 0
            while True:
                password.rotate(-1)
                r += 1
                i = ''.join(password).find(cc[-1])
                if i >= 4:
                    i += 2
                else:
                    i += 1
                if i == r:
                    break
    elif cc[0] == 'reverse':
        x = int(cc[2])
        y = int(cc[-1])
        p = list(password)
        password = deque(p[0:x] + p[x:y+1][::-1] + p[y+1:])
    elif cc[0] == 'move':
        y = int(cc[2])
        x = int(cc[-1])
        c = password[x]
        del password[x]
        password.insert(y, c)

print(''.join(password))