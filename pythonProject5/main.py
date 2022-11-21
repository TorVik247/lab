import math

AG=[0,1,1,0,0,0,
    1,0,1,1,1,0,
    1,1,0,1,1,0,
    0,1,1,0,1,1,
    0,1,1,1,0,1,
    0,0,0,1,1,0]
AG_=[]
j=int(math.sqrt(len(AG)))
i=0

while i<len(AG):

    #c=(AG[b]+AG[b1])+c
    #AG_.append(c)
    i=i+1
print(AG_)