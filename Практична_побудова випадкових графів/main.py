import random
n=8 #кількість вершин графу
m=8 #кількість ребер графу
i=0
listSum=[]
listOri=[]
listPov=[]

while i<(n ** 2):  #створює список нулів
    listSum.append(0)
    listOri.append(0)
    i=i+1
i=0
while i<m:
    sim=random.randint(1,(7))
    one=random.randint(1,(7))
    ranSim=((sim-1)*8)+one
    ranOne=(one*8)-1+sim
    if (ranOne==0 or ranOne%9==0) or((listPov.count(ranOne)>0)or(listPov.count(ranSim)>0)): #щоб по діагоналі було порожньо + щоб числа не повторялись
        continue
    else:
        listSum.pop(ranSim)
        listSum.insert(ranSim,1)
        listSum.pop(ranOne)
        listSum.insert(ranOne,1)
        listOri.pop(ranOne)
        listOri.insert(ranOne,1)
        listPov.append(ranOne)
        listPov.append(ranSim)
    i=i+1

print("Неорієнтований Граф")
for j in listSum:   #вивод
    if i>n-1:
        print()
        i=0
    print(j, end=" ")
    i=i+1
print()
print("Орієнтований Граф")
for j in listOri:   #вивод
    if i>n-1:
        print()
        i=0
    print(j, end=" ")
    i=i+1
