import math

AGC=[0, 1, 1, 0, 0, 0,
     1, 0, 1, 1, 1, 0,
     1, 1, 0, 1, 1, 0,
     0, 1, 1, 0, 1, 1,
     0, 1, 1, 1, 0, 1,
     0, 0, 0, 1, 1, 0]

AGG=[]
j=int(math.sqrt(len(AGC)))
one=0
c=0
k=0


while True:
    if (AGC.count(0)<=j):
        break
    else:
        for o in range(j):
            i = 0
            six = 0
            while i < j:
                while k < j - 1:
                    c = (AGC[one] * AGC[six]) + c
                    one = one + 1
                    six = six + j
                    k = k + 1
                AGG.append(c)
                one = one - (j - 1)
                six = six - (((j - 1) * j) - 1)
                c = 0
                k = 0
                i = i + 1
            one = one + j
        one = 0
        c = 0
        k = 0
        o=0
        i=0
        six=0
        for p in range((j*j)-1):
            if (p==six):
                six+=j+1
                continue
            elif(AGC[p] == 0):
                AGC.pop(p)
                AGC.insert(p, AGG[p])
        AGG.clear()

i=0#нема смисла виводити має бути   Матрицю відстаней
k=0
for k in AGC:
    if i > j - 1:
        print()
        i=0
    print(k, end=" ")
    i=i+1
