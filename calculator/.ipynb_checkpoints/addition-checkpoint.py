def add():
    l=[]
    ADDITION=0
    while(True):
        NUM=input("enter the number:")
        if(NUM=="+"):
            for i in range(len(l)):
                li=int(l[i])
                ADDITION=ADDITION+li
            print(ADDITION)
            break
        else:
            l.append(NUM)
add()