# ATM

**Description**:
This is a simple ATM python code where the user must enter a PIN to access their account balance, if the user fails to input the code too many times, the account will get locked.

**Features**:
- 3 PIN verification attempts
- Account locks after 3 failed attempts
- Displays the account balance after success pin input

## Installing the ATM Script:
You can install the ATM script by either copying the file from the respository or by copying this example code: 

```python
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
```
## Running the ATM Script: 
To run the ATM python script, you can input "python atm.py" in the editor terminal.

## ATM output:
Once the installation is complete and it's running, the user should be greeted by some propmts, which will look like this: 
```python
Please enter your PIN: 0000
Invalid PIN. Please try again.
Please enter your PIN: 0000
Invalid PIN. Please try again.
Please enter your PIN: 0000
Account locked. The police is on its way.
```
