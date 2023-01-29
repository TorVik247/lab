A = {21, 19, 14, 10, 8, 4}
A=list(A)
A.sort()
list.reverse(A)
B=37
Aji=[]
i=0
j=i
ji=j

while True:
    j=j+1
    ji=j+1
    if A[i]==A[-2]:
        break
    if A[i]==B:
        print(A[i])
    elif A[i]>B:
        if A[i]==A[-3]:
            break
        i=i+1
        j=i+1
        ji=j+1
    else:
        while True:
            Aji.append(A[i])
            Aji.append(A[j])
            if Aji[-1]==A[-1]:
                i=i+1
                j=i
                Aji.clear()
                break
            if sum(Aji) == B:
                print(Aji)
                j=j+1
                break
            elif sum(Aji) > B:
                Aji.clear()
                break
            else:
                while True:
                    Aji.append(A[ji])
                    if sum(Aji) == B:
                        print(Aji)
                        if A[ji]==A[-1]:
                            j=j+1
                            ji=j+1
                            Aji.clear()
                            break
                        elif A[ji]!=A[ji+1]:
                            j = j + 1
                            ji = j + 1
                            Aji.clear()
                            break
                        Aji.pop()
                        ji = ji + 1
                    elif sum(Aji) > B:
                        if Aji[-1]==A[-1]:
                            break
                        Aji.pop()
                        ji=ji+1
                    if Aji[-1] == A[-1]:
                        Aji.clear()
                        j=j+1
                        break