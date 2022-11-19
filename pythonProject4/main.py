list_sum=[]
list_ind=[]
i=0
j=0
u =0

X =5 #int(input())           #вершини графу
U =7 #int(input())           #кількість ребер графу
while i<((X ** 2)):                 #створює список нулів
    list_sum.append(0)
    i=i+1
i=0
while i<(X*U):
    list_ind.append(0)
    i = i + 1
i=0
while i<U:
    vid=input() #дані водяться у форматі х1х2
    vid_=int (vid[1:2]) #бере 1 із х1х2
    do=int (vid[3:]) #бере 2 із х1х2
    vid1=vid_ #копії для  матриці Інцидентності
    do1=do

    while True: #матриця Інцидентності
        vid_ = (vid_-1) * U + u
        do = (do-1)*U+u
        list_ind.pop(vid_)
        list_ind.insert(vid_, 2) #замість -1 в матриці Інцидентності пишу 2 щоб таблиця не деформувалась
        list_ind.pop(do)
        list_ind.insert(do, 1)
        u=u+1
        break

    if vid1>1:
        vid1 = (vid1 - 1) * X
        do1=vid1+do1
    do1=do1-1
    list_sum.pop(do1) #в списку звільняє місце під 1
    list_sum.insert(do1, 1)#вставляє в це місто
    i=i+1
i=0

print('Матриця Суміжності')

j=0
for j in list_sum: #вивод Матриця Суміжності
    if i>X-1:
        print()
        i=0
    print(j, end=" ")
    i=i+1

print()
print('Матриця Інцидентності')

j=0
i=0
for j in list_ind:#вивод Матриця Інцидентності
    if i>U-1:
        print()
        i=0
    print(j, end=" ")
    i=i+1