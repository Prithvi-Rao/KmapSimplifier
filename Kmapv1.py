s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # to write the final minterms expansion

n = int(input()) # number of variables in the k-map
A = list(map(int,input().split(' '))) # input 2^n integers , 0 or 1 to represent the 'i'th minterm

#converting array A into array B with the minterms
B = []
C = set()
for i in range(len(A)):
    if(A[i] == 1):
        t = bin(i)[2:]
        t = (n-len(t))*'0'+t# normalising number of bits
        B.append(t)
        C.add(t)

# returns the number of different bits in the binary representation of the two minterms
def diff(a,b):
    if(len(a) != len(b)):
        return n+1
    c = 0
    l = []
    for i in range(len(a)):
        if(a[i] != b[i]):
            c += 1
            l.append(i)
    return (c,l)

# function which performs one set of reductions
def step(B):
    D = []
    done = []
    for i in range(len(B)):
        for j in range(i+1,len(B)):
            (c,l) = diff(B[i],B[j])
            if(c == 1):
                a = B[i][:l[0]]+'X'+B[i][l[0]+1:]
                D.append(a)
                done.append(B[i])
                done.append(B[j])
            elif(c == 0):
                D.append(B[i])
                done.append(B[i])
    for i in B:
        if(i not in done):
            D.append(i)
    return D

# converting the binary representions into minterm form
def minterm(A):
    global s
    res = ''
    for i in range(len(A)):
        if(A[i] == '0'):
            res += s[i] + '\''
        elif (A[i] == '1'):
            res += s[i]
    return res

minterms = []
for i in B:
    minterms.append(minterm(i))

# perform reductions n+1 times( 1 extra time to remove copies)
for i in range(n+1):
    J = step(B)
    if(J == B):
        break
    else:
        B = J

#print(B)

minterms = []
for i in B:
    minterms.append(minterm(i))
for i in minterms[:-1]:
    print(i,end ='+')
print(minterms[-1])