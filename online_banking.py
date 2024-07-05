import math

def create_account():
    name = input("Create your username: ")
    pin = input("Create your password (6 digits): ")
    
    while len(pin) != 6 or not pin.isdigit():
        print("The password must be exactly 6 digits and numeric.")
        pin = input("Create your password (6 digits): ")
    
    print(f"Thanks, {name}. Your account is created.")
    return name, pin

def reset_pin():
    new_pin = input("Please create your new password (6 digits): ")
    
    while len(new_pin) != 6 or not new_pin.isdigit():
        print("Password must be exactly 6 digits and numeric.")
        new_pin = input("Create your new password (6 digits): ")
    
    print("The new password has been stored. Please login.")
    return new_pin

def calculate_compound_interest(principal, rate, time):
    principal = float(principal)
    rate = float(rate)
    time = float(time)
    
    # Compound interest formula: A = P * e^(rt)
    amount = principal * math.exp(rate * time)
    return amount

# Main script execution
print("Welcome to my online banking app!")

# Create an account
name, pin = create_account()

# Example of resetting PIN (if needed)
# pin = reset_pin()

# Calculate compound interest
principal = 1000  # Example principal amount
rate = 0.038  # Example annual interest rate
time = 6  # Example time in years

future_value = calculate_compound_interest(principal, rate, time)
print(f"The future value of the investment is: {future_value:.2f}")

def login():
    name1=str(print("enter your username "))
    pin1=str(print("enter your password "))
    if name1 == name and pin1 == pin:
        print(f"welcome! {name}")
    else:
        print("username or password is invalid")    



