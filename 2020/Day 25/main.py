with open('data.txt') as f:
    pub1, pub2 = [int(x) for x in f.read().strip().split('\n')]

n=1
loop_size = 0

while n!=pub2:
    n = (n*7)%20201227
    loop_size += 1

print(pow(pub1, loop_size, 20201227))