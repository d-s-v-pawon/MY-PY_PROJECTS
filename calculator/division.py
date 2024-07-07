def div():
    x=float(input("ENTER NUMERATOR:"))
    y=float(input("ENTER THE DENOMINATOR:"))
    print("NUMERATOR:",x)
    print("DENOMINATOR:",y)
    DIVISION=x/y
    print("DIVISION FOR FIRST TWO NUMBERS:",DIVISION)
    while(True):
        z=input("ENTER ANOTHER NUMBER:")
        print("ANOTHER NUMBER ENTERED FOR DIVISION:",z)
        if (z=="/"):
            break
        DIVISION=DIVISION/float(z)
    print("FINAL DIVISION",DIVISION)
div()