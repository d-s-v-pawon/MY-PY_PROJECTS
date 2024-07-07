def mul():
    l=[]
    while(True):
        NUM=input("enter the number:")
        print("ENTERED NUMBER FOR MULTIPLICATION:",NUM)
        if(NUM=="*"):
            for i in range(1,len(l)):
                li=int(l[i])
                MULTIPLICATION=MULTIPLICATION*li
            print("RESULT=",MULTIPLICATION)
            break
        else:
            l.append(NUM)
        MULTIPLICATION=int(l[0])
mul()