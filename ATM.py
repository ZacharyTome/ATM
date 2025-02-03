def atm():  # defines a function and calls it atm
    correct_pin = "1234"  # sets the correct PIN to "1234"
    attempts = 3  # defines the maximum number of attempts(3)

    while attempts > 0:  # begins a loop
        pin = input("Please enter your PIN: ")  # prompts the user to enter their PIN
        if pin == correct_pin:  # checks if pin = correct_pin
            print("Your account balance is: 0. Goodbye!")  # prompts account balance
            return
        else:
            attempts -= 1  # decreases the number of attempts by 1
            if attempts > 0:  # checks if there are attempts left
                print("Invalid PIN. Please try again.")  # prompts the user to try again
            else:  # executes when there are no more attempts left
                print("Account locked. The police is on its way.")

atm()  # calls the function