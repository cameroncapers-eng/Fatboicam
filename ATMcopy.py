CORRECT_PIN = "1201"

pin = input("Enter your 4-digit PIN: ")

checking_balance = 2130.78
savings_balance = 64201032.99

if pin == CORRECT_PIN:
    print("\nPIN accepted.")
    print("Choose an account:")
    print("1. Checking")
    print("2. Savings")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nYou selected Checking.")
        print("Welcome to your Checking account!")
        print(f"Your checking balance is: ${checking_balance:.2f}")
    elif choice == "2":
        print("\nYou selected Savings.")
        print("Welcome to your Savings account!")
        print(f"Your savings balance is: ${savings_balance:.2f}")

    else:
        print("\nInvalid selection.")
else:
    print("\nIncorrect PIN. Access denied.")

