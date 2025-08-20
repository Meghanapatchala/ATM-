users = {"62433570421": ["user1", 5000, 1234],
         "62433570422": ["user2", 500, 4567],
         "62433570423": ["user3", 15000,9870],
         "62433570424": ["user4", 1000, 3789],
         "62433570425": ["user5", 600, 1470]
         }
print("***Welcome to ATM***")
print()

user_account = input("enter your account number: ")
transactions = []
if user_account in users:
    max_attempts = 3
    attempt = 1
    active_session = False
    while attempt<=max_attempts:
        user_pin = int(input("Enter your pin: "))
        if user_pin == users[user_account][-1]:
            print("Login successful.you can proceed with transaction")
            active_session = True
            break
        else:
            remaining_attempts = max_attempts - attempt
            
            if remaining_attempts == 0:
                  
                 print("Account Locked.visit your branch")
            else:
                      print(f"Incorrect pin.you have {remaining_attempts}attempts left")
            attempt += 1
    while True and active_session:
                print("choose any option from the given: ")
                print("1.Deposit")
                print("2.withdraw")
                print("3.Transaction history")
                print("4.Balance enquiry")
                print("5.Pin change")
                print("6.Exit")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = int(input("Enter the amount you want to deposit: "))
                    if amount>0:
                        
                       users[user_account][1] += amount
                       print("Amount deposited")
                       transactions.append(f"{amount} deposited")
                       print(f"Balance is {users[user_account][1]}")
                elif choice == 2:
                    amount = int(input("please enter the amount: "))
                    if amount<=users[user_account][1]:
                        users[user_account][1] -= amount
                        print("collect your cash")
                        transactions.append(f"{amount} withdraw")
                        print(f"balance: {users[user_account][1]}")
                    else:
                        print("Insufficient funds")
                    print("Please enter a valid amount")
                elif choice == 3:
                    for transaction in transactions[::-1]:
                        print(transaction)
                elif choice == 4:
                    print(f"balance: {users[user_account][1]}")
                elif choice == 5:
                    userpin = int(input("Enter your current pin: "))
                    if userpin == users[user_account][-1]:
                        new_pin = int(input("please enter your new pin: "))
                        confirm = int(input("please confirm your pin: "))

                        if new_pin == confirm:
                            users[user_account][-1] = new_pin
                            print("pin changed")
                        else:
                            print ("pin confirmation unsuccessful: ")
                    else:
                        print("invalid pin")
                elif choice == 6:
                    print()
                    print("Thank you. Visit again")
                    print()
                    break
                else:
                    print ("Invalid choice.")
                
            
else:
    print("Invalid account")
