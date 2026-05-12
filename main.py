balance = 5000000
PIN = "2345"

print("WELCOME TO ATM")
user_pin = input("Enter the PIN ::")

if user_pin == PIN:
    while True:
        
        print("\n1. Check balance")
        print("2. Deposite")  
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice ::")
        
        if choice == "1":
            print("Your Balance is", balance)
         
        elif choice == "2":
            amount = int(input("Enter amount to deposite"))
            balance += amount
            print("Amount deposited successfully ")
            
        elif choice == "3":
            amount = int(input("Enter amount to withdraw ::"))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
            else:
                print("Insufficient balance")
                
        elif choice == "4":
            print("Thank you for using ATM")
            break
        
        else:
            print("Invalid choice")
else:
    print("wrong PIN")

