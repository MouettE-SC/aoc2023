from hashlib import md5
from collections import deque

salt = open('day-14.input', 'r').read()

i = 0
potential_keys = {}
keys = 0
hashes = deque()
for j in range(1000):
    hashes.append(md5(f'{salt}{j}'.encode()).hexdigest())

while keys < 64:
    print(f'\r{i} {keys}', end='', flush=True)
    h = hashes.popleft()
    hashes.append(md5(f'{salt}{i+1000}'.encode()).hexdigest())
    pk = ''
    for j in range(len(h)-2):
        if h[j]*3 == h[j:j+3]:
            pk = h[j]*5
            break
    if pk:
        for h2 in hashes:
            if pk in h2:
                keys += 1
                if keys == 64:
                    print(f"\r{i}   ")
                    exit(0)
    i += 1