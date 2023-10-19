# All Rights Reserved | Copyright (c) 2023 yesha
#-------------------------------------------------------
# Program to Calculate Total Amount Due For Car Purchase, Including Basic Price, Finish, Accessories, and Trade-in Value.
#-------------------------------------------------------
# Created by; yesha
#-------------------------------------------------------
# Date; March 1st 2023
#-------------------------------------------------------


from array import *
import os


def clear_screen():       # Function to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI escape codes for green and white text
green_text = "\033[32m"
white_text = "\033[97m"


welcome_message = f"""
{green_text}
  ____      _    _______ _   _ 
 |  _ \\    | |  |__   __| \\ | |
 | |_) |__ | | __ _| |  |  \\| |
 |  _ < _ \\| |/ _` | |  | . ` |
 | |_) |_) | | (_| | |  | |\\  |
 |____/.__/|_|\\__,_|_|  |_| \\_|{white_text}
Welcome to the Car Purchase Calculator!
"""       # ASCII art for the welcome message in green and white

clear_screen()       # Clear the screen and display the welcome message
print(welcome_message)


def get_price(prompt):       # Get the basic price of the car
    while True:
        price = input(prompt)
        try:
            price = float(price)
            return price
        except ValueError:
            print("Invalid input, please enter a number.")


def get_trade_in_price(prompt):    # Get the trade in price of the car if the user didn't enter anything the trade in price is 0
    trade_in = 0.0
    while True:
        price = input(prompt)
        if price == "":
            return trade_in
        try:
            price = float(price)
            if price < 0:
                print("Trade-in value cannot be negative. Please enter a valid trade-in value.")
            else:
                trade_in = price
                return trade_in
        except ValueError:
            print("Invalid input, please enter a number.")


def get_choice(prompt):     # Get the choice of the user (y/n)
    while True:
        choice = input(prompt)
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'.")


def get_finish_price():     # Get the finish price of the car (standard, modified, customized)
    while True:
        finish = input("Select exterior finish (S for standard, M for modified, C for customized): ")
        if finish.lower() == 's':     # If the user enter 's' OR 'S' the price of the standard finish will be returned
            return 0
        elif finish.lower() == 'm':
            return 370.50
        elif finish.lower() == 'c':
            return 1257.99
        else:
            print("Invalid input, please enter 'S', 'M', or 'C'.")


def accessories_edit(accessory_prices):     # Edit the accessories price (stereo system, leather interior, GPS)
    while True:
        choice = input('Select accessory to edit (S for Stereo system, L for leather interior, G for GPS): ')
        if choice.lower() == 's':     # If the user enter 's' OR 'S' the price of the stereo system will be changed
            accessory_prices[0] = float(input("Enter new stereo system price: "))
        elif choice.lower() == 'l':   
            accessory_prices[1] = float(input("Enter leather interior price: "))
        elif choice.lower() == 'g':
            accessory_prices[2] = float(input("Enter GPS price: "))
        else:
            print("Invalid input, please enter 'S', 'L', or 'G'.")
            continue
        if not get_choice('Do you want to edit another accessory? (y/n)'):
            break


def accessories_display(accessory_prices):    # Display the accessories price 
    print("Stereo system price\t" + str(accessory_prices[0]) +
          "\nLeather interior price\t" + str(accessory_prices[1]) +
          "\nGPS price\t\t" + str(accessory_prices[2]))


def calculate_amount_due(basic_price, accessory_chosen_p, finish_price, trade_in):     # Calculate the amount due
    subtotal = basic_price + sum(accessory_chosen_p) + finish_price
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    amount_due = subtotal + sales_tax - trade_in
    return amount_due


def get_accessory_chosen_p(accessory_prices):     # Get the accessories chosen by the user 
    accessory_chosen_p = []
    if get_choice("Do you want to add a stereo system? (y/n) "):
        accessory_chosen_p.append(accessory_prices[0])
    if get_choice("Do you want to add leather interior? (y/n) "):
        accessory_chosen_p.append(accessory_prices[1])
    if get_choice("Do you want to add GPS? (y/n) "):
        accessory_chosen_p.append(accessory_prices[2])
    return accessory_chosen_p


def Calculate (accessory_prices):    # Calculate the amount due
    basic_price = get_price("Enter basic price: ")
    trade_in = get_trade_in_price("Enter trade-in allowance (press Enter for 0): ") 

    accessories_display(accessory_prices)

    if get_choice('Do you want to edit accessories price ? (y/n)'):
        accessories_edit(accessory_prices)

    accessory_chosen_p = get_accessory_chosen_p(accessory_prices)

    finish_price = get_finish_price()

    amount_due = calculate_amount_due(basic_price, accessory_chosen_p, finish_price, trade_in)
    print("Amount Due: ", amount_due)


def CLear_values(accessory_prices):     # Clear the values (accessories price set to 0)
    accessory_prices =[0,0,0]
    print("Values have been cleared")
    return accessory_prices


def Reset(accessory_prices):      # Reset the values (accessories price reset to the given values)
    accessory_prices = [30.50, 530.99, 301.90]
    print("Values have been reset")
    return accessory_prices


def Exit():    # Exit the program
    exit()


def main():      # Main function

    accessory_prices = [30.50, 530.99, 301.90]

    while True:
        print("1. Calculate")
        print("2. Clear values")
        print("3. Reset")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            Calculate(accessory_prices)
        elif choice == '2':
             accessory_prices =CLear_values(accessory_prices)
        elif choice == '3':
             accessory_prices =Reset(accessory_prices)
        elif choice == '4':
            Exit()
        else:
            print("Invalid input, please enter '1', '2', '3' or '4'.")


if __name__ == '__main__':     # Call the main function
    main()

