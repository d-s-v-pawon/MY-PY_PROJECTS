def sub():
    l=[]
    while(True):
        NUM=input("enter the number:")
        print("ENTERED NUMBER FOR SUBTRACTION:",NUM)
        if(NUM=="-"):
            for i in range(1,len(l)):
                li=int(l[i])
                if(li<0):
                    SUBTRACTION=SUBTRACTION+li
                else:
                    SUBTRACTION=SUBTRACTION-li
            print("RESULT=",SUBTRACTION)
            break
        else:
            l.append(NUM)
        SUBTRACTION=int(l[0])
sub()