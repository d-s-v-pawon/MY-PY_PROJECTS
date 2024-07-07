def add():
    l=[]
    ADDITION=0
    while(True):
        NUM=input("enter the number:")
        print("ENTERED NUMBER FOR ADDITION:",NUM)
        if(NUM=="+"):
            for i in range(len(l)):
                li=int(l[i])
                ADDITION=ADDITION+li
            print("TOTAL=",ADDITION)
            break
        else:
            l.append(NUM)
add()