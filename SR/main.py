A=['Erlang', 'Groovy', 'Delphi', 'Pascal', 'Ruby', 'PHP','Swift', 'Python', 'Go']
masuvA=[]
i=0
j=0
n=0
ryadok=[]
#ord
while i<len(A):
    Aq = A[i]
    Aq =list(Aq)
    masuvA.append(Aq)
    i=i+1
i=1
print(A[0])
while i<len(A):
    n=0
    Arra=ord(masuvA[j][n])#
    ora=ord(masuvA[i][n])#arr_A[слово][буква]перевірка

    if Arra<ora:
        print("\\"+A[i])
    elif Arra>ora:
        print("/" +A[i])
    elif Arra==ora:#==
        while True:
            n=n+1
            Arra = ord(masuvA[j][n])  #
            ora = ord(masuvA[i][n])  # arr_A[слово][буква]перевірка
            if Arra < ora:
                print("\\" + A[i])
            elif Arra > ora:
                print("/" + A[i])
    i=i+1
    j=j+1
