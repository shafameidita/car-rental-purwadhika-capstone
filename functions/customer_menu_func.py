from tabulate import tabulate
import textwrap

def customer_menu (car_list, cart, login_page) :
    while (True): 
        try : 
            print ('''
        Welcome to ABC Rent Car,
        "Your satisfaction is our priority"
                    
        Please choose one option: 
        1. Show Car List 
        2. Rent Car 
        3. Back to the login page 
        4. Exit Program               
        ''')
            cust_input = int(input('write the number here: '))
            if cust_input == 1:
                search_car_list (car_list, cart, login_page)
            elif cust_input == 2: 
                cust_menu_rent(car_list, cart, login_page)
            elif cust_input == 3: 
                login_page()
            elif cust_input == 4: 
                exit() 
            else : 
                print('Please enter the correct number! ') 
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def show_car_list(car_list): 
     print('''      
                                Car List 
                        ''')
     print(tabulate(car_list, headers="keys", tablefmt="rounded_grid"))

def search_car_list (car_list, cart, login_page): 
     show_car_list(car_list)
     while(True):
        search_car = input('Do you want to search any car? (y/n) : ').lower()
        if search_car == 'y': 
            result = {key: [] for key in car_list}
            while(True): 
                model_to_search = input('Please enter car\'s model here : ').title().strip()
                if model_to_search in set([i.title().strip() for i in car_list["Model"]]): 
                    print('Thank you, this is the result : ')    
                    for i in range(len(car_list["Model"])):
                        if car_list["Model"][i].title().strip() == model_to_search:
                            result['No'].append(car_list['No'][i])
                            result['Model'].append(car_list['Model'][i])
                            result['Type'].append(car_list['Type'][i])
                            result['Capacity'].append(car_list['Capacity'][i])
                            result['Stock'].append(car_list['Stock'][i])
                            result['Price/day'].append(car_list['Price/day'][i])

                    print(tabulate(result, headers="keys", tablefmt="rounded_grid"))
                    break 
                else: 
                    print('Car is not available, please input the correct car\'s model')


        elif search_car == 'n': 
            print('Thank you, you will be directed to the Customer Menu')
            customer_menu(car_list, cart, login_page)
            break
        
        else :
            print('Please enter a valid input') 
            continue


def cust_menu_rent(car_list, cart, login_page): 
     total_payment = 0
     show_car_list(car_list)
     while(True) :     
        try:               
            cust_car = int(input('Write the car\'s number: '))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue 
        if cust_car not in car_list["No"]:
            print('Invalid input! Please enter a valid number.')
            continue
        else: 
            while(True): 
                try:
                    rent_day = int(input('How many days: '))
                    if rent_day > 7 : 
                        print('Maximum rent period is 7 days, please try again.') 
                        continue
                    elif rent_day == 0 : 
                        print('The amount of day can not be zero')
                    else: 
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

            index_car = car_list['No'].index(cust_car)
            cart["No"].append(cust_car)
            cart_num= len(cart['No'])
            cart['No'] = [i+1 for i in range(cart_num)]

            cart["Model"].append(car_list["Model"][index_car])
            cart["Type"].append(car_list["Type"][index_car])
            cart["Price/day"].append(car_list["Price/day"][index_car])
            cart["Total Day"].append(rent_day)
            cart["Total Price"].append(rent_day*car_list["Price/day"][index_car])
            print(tabulate(cart, headers="keys", tablefmt="rounded_grid"))
            total_payment += rent_day * car_list["Price/day"][index_car]

            if cust_car in car_list['No'] and car_list['Stock'][index_car] == 1:
                car_list["No"].pop(index_car)
                car_list["Model"].pop(index_car)
                car_list["Type"].pop(index_car)
                car_list["Capacity"].pop(index_car)
                car_list["Stock"].pop(index_car)
                car_list["Price/day"].pop(index_car)
                num_remaining_cars = len(car_list['No']) 
                car_list['No'] = [i+1 for i in range(num_remaining_cars)]

            elif cust_car in car_list['No'] and car_list['Stock'][index_car] > 1: 
                car_list['Stock'][index_car] -= 1 
                num_remaining_cars = len(car_list['No']) 
                car_list['No'] = [i+1 for i in range(num_remaining_cars)]

        
            while(True): 
                cart_input = input('Do you want to add more car? (y/n): ').lower()
                if cart_input == 'y' : 
                    selected_car = car_list['No'].index(cust_car)
                    show_car_list(car_list)
                    break
                   
                elif cart_input == 'n': 
                    while(True): 
                        print(f'The total is {total_payment}' )
                        try: 
                            user_payment = int(input('Input your payment: '))
                            change = int(user_payment - total_payment)
                            if user_payment >= total_payment:
                                    str_return_money = f'''
                                        Thank You,

                                        Your return is: {change}
                                    '''
                                    print(textwrap.dedent(str_return_money))
                                    final_input = input('Do you want to leave the program? (y/n): ').lower()
                                    if final_input == 'y': 
                                        exit()
                                    elif final_input == 'n': 
                                        print('Thank you, you will be directed to the Customer Menu')
                                        for key in cart.keys():
                                            cart[key] = []
                                        customer_menu (car_list, cart, login_page)
                                    else : 
                                        print('Please enter the correct input, y for yes and n for no.')

                            else: 
                                print(f'Not enough, please add more {total_payment - user_payment}')
                                while(True): 
                                    cancel_rent = input('do you want to cancel your order? (y/n): ').lower()
                                    if cancel_rent == 'y': 
                                        print('Thank you, you will be directed to the Customer Menu')

                                        while cart["No"]:
                                            cancelled_car_index = cart["No"].pop()
                                            cancelled_car_index_in_car_list = car_list["No"].index(cancelled_car_index)
                                            car_list["Model"].insert(cancelled_car_index_in_car_list, cart["Model"].pop())
                                            car_list["Type"].insert(cancelled_car_index_in_car_list, cart["Type"].pop())
                                            car_list["Capacity"].insert(cancelled_car_index_in_car_list, car_list["Capacity"][cancelled_car_index_in_car_list])
                                            car_list["Stock"].insert(cancelled_car_index_in_car_list, 1)
                                            car_list["Price/day"].insert(cancelled_car_index_in_car_list, cart["Price/day"].pop())

                                            car_list["No"].insert(cancelled_car_index_in_car_list, cancelled_car_index)

                                        cart["Total Day"].clear()
                                        cart["Total Price"].clear()

                                        car_list["No"] = [i + 1 for i in range(len(car_list["No"]))]

                                        customer_menu(car_list, cart, login_page)

                                                                                
                                    elif cancel_rent == 'n': 
                                        break
                                    else: 
                                        print('Please enter the correct input, y for yes and n for no.')
                                        continue     
       
                        except ValueError:
                            print("Invalid input! Please input the right payment amount.")
                            continue
              

                            
                else: 
                    print('Wrong answer, please try again.')
                    continue
                break