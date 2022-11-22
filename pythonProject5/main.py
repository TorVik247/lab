import math

AG=[0,1,1,0,0,0,
    1,0,1,1,1,0,
    1,1,0,1,1,0,
    0,1,1,0,1,1,
    0,1,1,1,0,1,
    0,0,0,1,1,0]

AG_=[]
j=int(math.sqrt(len(AG)))
one=0
c=0
k=0

for o in range(6):
    i=0
    six=0
    while i<j:
        while k<j-1:
            c = (AG[one] * AG[six]) + c
            one = one + 1
            six = six + j
            k=k+1
        AG_.append(c)
        one= one - (j-1)
        six = six - (((j-1)*j)-1)
        c = 0
        k = 0
        i=i+1
    one=one +j

i=0#нема смисла виводити має бути   Матрицю відстаней
k=0
for k in AG_:
    if i>j-1:
        print()
        i=0
    print(k, end=" ")
    i=i+1
