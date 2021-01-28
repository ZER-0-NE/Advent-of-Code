with open('data.txt') as f:
    inp = list(map(int, f.read()))

p1 = inp.copy()
p2 = inp.copy()

def part1(fft):
    A = [0 for _ in range(len(fft))]
    D = [0] + fft

    for i in range(len(A)):
        ans = 0
        for j in range(len(D)):
            block = (j//(i+1))%4
            mult = {0:0, 1:1, 2:0, 3:-1}[block]
            A[i] += D[j] * mult
    A = [abs(x)%10 for x in A]
    return A

for i in range(100):
    p1 = part1(p1)

print(f"1. {''.join([str(p1[i]) for i in range(8)])}")


p2 = p2 * 10000
offset = int(''.join([str(p2[i]) for i in range(7)]))

def part2(fft):
    A = [0 for _ in range(len(fft))]
    ans = 0

    for i in range(1, len(fft)//2):
        ans += fft[-i]
        A[-i] = ans
    A = [abs(x)%10 for x in A]
    return A

for _ in range(100):
    p2 = part2(p2)

print(f"2. {''.join([str(p2[i]) for i in range(offset, offset+8)])}")

# another sol; credits to bluepichu

# The key observation for part 2 is that if your sequence has length n and you want to compute the 
# value of the next phase at index i with i > n/2, then it's just the sum of all of the elements 
# with index at least i. Therefore, we only need to compute the sequence for indices higher than 
# the given offset at every phase, and we can do so in linear time.

def do_phase(lst):
    return [do_comp(lst, i) for i in range(len(lst))]

def get_mult(n, m):
    m += 1
    m %= 4*n
    if m<n:
        return 0
    elif m<2*n:
        return 1
    elif m<3*n:
        return 0
    elif m<4*n:
        return -1

def do_comp(lst, idx):
    idx +=1
    out = 0

    for i in range(len(lst)):
        out += lst[i] * get_mult(idx, i)

    return int(str(out)[-1:])

for i in range(100):
    p1 = do_phase(p1)

print(f"1. {''.join(map(str, p1[:8]))}")

def do_phase2(inp):
    s = sum(inp)
    out = []
    for i in range(len(inp)):
        out += [((s%10) + 10)%10]
        s -= inp[i]

    return out

offset = int(''.join(map(str, p2[:7])))
p2 = p2 * 10000

p2 = p2[offset:]

for i in range(100):
    p2 = do_phase2(p2)

print(f"2. {''.join(map(str, p2[:8]))}")