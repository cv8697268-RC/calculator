def add(a,b):
    return a+b
def mul (a,b):
    return a-b
def sub(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

while True:
    a = int(input("Enter the first value ::"))
    b = int(input("Enter the second value ::"))
    
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. mod")
    print("6. exit")
       
    choice = int(input("Enter the ur choice::"))

    if choice == 1:
        print("add a and b",add(a,b))
        
    elif choice ==2:
        print("mul a and b",mul(a,b))
        
    elif choice ==3:
        print("sub a and b",sub(a,b))
    elif choice ==4:
        print("div a and b",div(a,b))
    elif choice == 5:
        print("mod a and b",mod(a,b))
    elif choice == 6:
        print("tnx welcome again")
        break
    else:
        print("Invalid choice")
    