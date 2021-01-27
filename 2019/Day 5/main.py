# credits to jonathon_paulson

OP = [int(x) for x in  open('data.txt').read().split(',')]

def get_args(P, ip, n, digits, output):
    while len(digits) < n:
        digits = [0]+digits
    ans = P[ip+1:ip+n+1]
    if output:
        assert digits[0] == 0
        digits[0] = 1
    ans = [x if digits[len(digits)-1-i]==1 else P[x] for i,x in enumerate(ans)]
    return ans


P = [x for x in OP]
ip = 0
while True:
    digits = [int(x) for x in str(P[ip])]
    opcode = (0 if len(digits)==1 else digits[-2])*10+digits[-1]
    digits = digits[:-2]
    if opcode == 1:
        i1,i2,i3 = get_args(P, ip, 3, digits, True)
        P[i3] = i1+i2
        ip += 4
    elif opcode == 2:
        i1,i2,i3 = get_args(P, ip, 3, digits, True)
        P[i3] = i1*i2
        ip += 4
    elif opcode == 3:
        i1 = P[ip+1]
        P[i1] = 5 # special input; change to 1 for part 1
        ip += 2
    elif opcode == 4:
        i1 = P[ip+1]
        print(P[i1])
        ip += 2
    elif opcode == 5:
        i1,i2 = get_args(P, ip, 2, digits, False)
        if i1!=0:
            ip = i2
        else:
            ip += 3
    elif opcode == 6:
        i1,i2 = get_args(P, ip, 2, digits, False)
        if i1==0:
            ip = i2
        else:
            ip += 3
    elif opcode == 7:
        i1,i2,i3 = get_args(P, ip, 3, digits, True)
        if i1 < i2:
            P[i3] = 1
        else:
            P[i3] = 0
        ip += 4
    elif opcode == 8:
        i1,i2,i3 = get_args(P, ip, 3, digits, True)
        if i1 == i2:
            P[i3] = 1
        else:
            P[i3] = 0
        ip += 4
    else:
        assert opcode == 99
        break
