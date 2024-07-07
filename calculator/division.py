def div():
    x=float(input("ENTER NUMERATOR:"))
    y=float(input("ENTER THE DENOMINATOR:"))
    DIVISION=x/y
    print(DIVISION)
    while(True):
        z=input("ENTER ANOTHER NUMBER:")
        if (z=="/"):
            break
        DIVISION=DIVISION/float(z)
    print(DIVISION)
div()