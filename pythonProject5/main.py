import math

AG1=[0, 1, 1, 0, 0, 0,
     1, 0, 1, 1, 1, 0,
     1, 1, 0, 1, 1, 0,
     0, 1, 1, 0, 1, 1,
     0, 1, 1, 1, 0, 1,
     0, 0, 0, 1, 1, 0]
AGG2=[0, 1, 1, 0, 0, 0,
     1, 0, 1, 1, 1, 0,
     1, 1, 0, 1, 1, 0,
     0, 1, 1, 0, 1, 1,
     0, 1, 1, 1, 0, 1,
     0, 0, 0, 1, 1, 0]
AGG=[]
AG2=[0, 1, 1, 0, 0, 0,
     1, 0, 1, 1, 1, 0,
     1, 1, 0, 1, 1, 0,
     0, 1, 1, 0, 1, 1,
     0, 1, 1, 1, 0, 1,
     0, 0, 0, 1, 1, 0]
j=int(math.sqrt(len(AG1)))
one=0
c=0
k=0


while True:
    if (AGG2.count(0)<=j):
        break
    else:
        for o in range(j):
            i = 0
            six = 0
            while i < j:
                while k < j - 1:
                    c = (AG1[one] * AG2[six]) + c
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
        for u in range((j*j)-1):
            AG2.pop(u)
            AG2.insert(u, AGG[u])
        AGG.clear()
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
            elif(AGG2[p] == 0):
                AGG2.pop(p)
                AGG2.insert(p, AG2[p])

i=0
k=0
for k in AGG2:
    if i > j - 1:
        print()
        i=0
    print(k, end=" ")
    i=i+1