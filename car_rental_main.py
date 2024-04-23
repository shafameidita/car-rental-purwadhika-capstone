from tabulate import tabulate
from functions.staff_menu_func import *
from functions.customer_menu_func import *


car_list = {
    "No" : [ 1, 2, 3, 4, 5, 6, 7, 8, 9], 
    "Model" : ['Toyota Calya', 'Daihatsu Sigra', 'Honda Brio', 'Daihatsu Ayla', 'Suzuki Ignis', 
               'Daihatsu Xenia', 'Suzuki Mobilio', 'Toyota Hiace', 'Wuling Air EV'], 
    "Type"  : ['Matic', 'Matic', 'Matic', 'Matic', 'Matic', 'Manual', 'Manual', 'Manual', 'Electric'], 
    "Capacity" : [7, 7, 5, 5, 5, 7, 7, 14, 4], 
    "Stock" : [1, 1, 1, 1, 1, 1, 1, 2, 2],
    "Price/day" : [700000, 700000, 500000, 500000, 500000, 600000, 600000, 1000000, 850000]
}

cart = {
    "No" : [],
    "Model" : [],
    "Type" : [], 
    "Price/day" : [],
    "Total Day" : [], 
    "Total Price" : []
}

cart_update = {
    "No" : [],
    "Model" : [],
    "Type" : [], 
    "Capacity" : [], 
    "Stock" : [],
    "Price/day" : [],
}

def login_page(): 
    print(''' 
    Welcome to ABC Rent Car 
    "Your satisfaction is our priority"
            
    confirm your identity: 
    1. Customer 
    2. Staff       
    ''')

    while (True) : 
        try:
            user_input = int(input('Write your number here: '))
            if user_input == 1: 
                customer_menu (car_list, cart, login_page)
                break
            elif user_input == 2: 
                staff_menu(car_list, cart_update, login_page)
                break
            else : 
                print('Please enter the correct number! ')
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    return user_input

login_page()
