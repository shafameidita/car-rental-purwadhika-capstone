from tabulate import tabulate
import textwrap 

def staff_menu(car_list, cart_update, login_page) : 
     while(True): 
        try :
            try:
                str_staff_page = ('''
                                  Welcome to the Staff Menu''')
                print(textwrap.dedent(str_staff_page))
                staff_id = int(input('Please enter your identity number: '))
                id_num = {123, 456, 789}
            except ValueError:
                print("Invalid input! Please enter a identity number.")
                continue
            
            if staff_id in id_num:
                print("Identity number is correct.")
                print (''' 
            Welcome to ABC Rent Car,
            "Your satisfaction is our priority"
                        
            Please choose one option: 
                1. Show Car List 
                2. Add Car List 
                3. Update Car List 
                4. Delete Car List 
                5. Back to login page                  
                6. Exit Program 
                        ''')
            else: 
                print("Wrong identity number! Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")

        staff_input = int(input('write the number here: '))
        if staff_input == 1 : 
            search_car_list (car_list, cart_update, login_page)
        elif staff_input == 2: 
            staff_menu_add (car_list, cart_update, login_page)
        elif staff_input == 3: 
            staff_menu_update (car_list, cart_update, login_page)
        elif staff_input == 4 : 
            staff_menu_delete (car_list, cart_update, login_page)
        elif staff_input == 5: 
            login_page()
        elif staff_input == 6: 
            exit()
        else : 
            print('Please enter the correct number!')

def show_car_list(car_list): 
     print('''      
                                Car List 
                        ''')
     print(tabulate(car_list, headers="keys", tablefmt="rounded_grid"))


def search_car_list (car_list, cart_update, login_page): 
     show_car_list(car_list)
     while(True):
        search_car = input('Do you want to search any car? (y/n) : ').lower()
        if search_car == 'y': 
            result = {key: [] for key in car_list}
            while(True): 
                model_to_search = input('Please enter car\'s model here : ').title()
                if model_to_search in car_list["Model"]:
                    print('Thank you, this is the result : ')    
                    for i in range(len(car_list["Model"])):
                        if car_list["Model"][i] == model_to_search:
                            row = [car_list[key][i] for key in car_list.keys()]
                            result['No'].append(row [0])
                            result['Model'].append(row [1])
                            result['Type'].append(row [2])
                            result['Capacity'].append(row [3])
                            result['Stock'].append(row [4])
                            result['Price/day'].append(row [5])

                    print(tabulate(result, headers="keys", tablefmt="rounded_grid"))
                    break 
                else: 
                    print('Car is not available, please input the correct car\'s model')


        elif search_car == 'n': 
            print('Thank you, you will be directed to the Staff Menu')
            staff_menu(car_list, cart_update, login_page)
            break
        
        else :
            print('Please enter a valid input') 
            continue

def staff_menu_add (car_list, cart_update, login_page): 
    while(True): 
        show_car_list(car_list)
        add_model = input('Add Car Model : ').title()
        add_type = input('Add Car Type: ').title() 
        while (True): 
            try:
                add_capacity = int(input('Add Car\'s Capacity: '))
                if add_capacity < 2 :
                    print('Minimal amount for capacity is 2, please try again.') 
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        while True:
            try:
                add_stock = int(input('Enter the Stock: '))
                if add_stock == 0 :
                    print('You can not enter 0 stock, please try again.') 
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number for Stock.")
        while True:
            try:
                add_price = int(input('Add price per day: '))
                if add_price == 0 :
                    print('You can not enter 0 for price/day, please try again.') 
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number for Price.")

        if (add_model, add_type, add_capacity, add_price) in zip(car_list["Model"], car_list["Type"], car_list["Capacity"], car_list["Price/day"]): 
            while(True): 
                same_item = input('Car is already in the list, maybe you want to update? (y/n): ').lower()
                if same_item == 'y': 
                    staff_menu_update (car_list, cart_update, login_page)
                    break
                elif same_item == 'n':
                    print('Update canceled, you will be directed to Staff Menu.')
                    staff_menu(car_list, cart_update, login_page) 
                    break
                else: 
                    print('Incorrect answer, please input y for yes, and n for no.')
                    continue

        new_numb = len(car_list['No'])+ 1 
        car_list['No'] = [i+1 for i in range(new_numb)]
        car_list['Model'].append(add_model)
        car_list['Type'].append(add_type)
        car_list['Capacity'].append(add_capacity)
        car_list['Price/day'].append(add_price)
        car_list['Stock'].append(add_stock)
        print ('Car successfuly added! ')
        show_car_list(car_list)

        while(True): 
            add_more_car = input('do you want to add more car? (y/n): ').lower()
            if add_more_car == 'y': 
                break
            elif add_more_car == 'n':
                print('Car successfuly added, you will be directed to the Staff Menu') 
                staff_menu(car_list, cart_update, login_page) 
                break
            else: 
                print('Incorrect answer, please input y for yes, and n for no.')
                continue

def staff_menu_update (car_list, cart_update, login_page): 
    while True:
        show_car_list(car_list)
        try:
            update_car = int(input('Enter the number of car you want to update: '))
        except ValueError:
            print("Invalid input! Please enter a correct number.")
            continue
        
        if update_car in car_list['No']:
            break
        else:
            print('Enter the correct number!')
            continue
    
    index_car = car_list['No'].index(update_car)
    cart_num= len(cart_update['No'])
    if cart_num == 0 : 
        cart_update["No"].append(update_car)
        cart_update["Model"].append(car_list["Model"][index_car])
        cart_update["Type"].append(car_list["Type"][index_car])
        cart_update["Capacity"].append(car_list["Capacity"][index_car])
        cart_update["Stock"].append(car_list["Stock"][index_car])
        cart_update["Price/day"].append(car_list["Price/day"][index_car])
        print(tabulate(cart_update, headers="keys", tablefmt="rounded_grid"))
        cart_num += 1

    else : 
        cart_update['No'][0] = update_car
        cart_update['Model'][0] = car_list['Model'][index_car]
        cart_update['Type'][0] = car_list['Type'][index_car]
        cart_update['Capacity'][0] = car_list['Capacity'][index_car]
        cart_update['Stock'][0] = car_list['Stock'][index_car]
        cart_update['Price/day'][0] = car_list['Price/day'][index_car]
        print(tabulate(cart_update, headers="keys", tablefmt="rounded_grid"))
        
    update_index = car_list['No'].index(update_car)
    car_list['Model'][update_index] = input('Enter new Model: ').title()
    car_list['Type'][update_index] = input('Enter new Type: ').title()
    while (True): 
        try:
            car_list['Capacity'][update_index] = int(input('Enter new Capacity: '))
            if car_list['Capacity'][update_index] < 2 :
                print('Minimal amount for capacity is 2, please try again.') 
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number of Capacity.")
    while True:
        try:
            car_list['Stock'][update_index] = int(input('Enter new Stock: '))
            if car_list['Stock'][update_index] == 0 :
                print('You can not enter 0 stock, please try again.') 
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for Stock.")
    while True:
        try:
            car_list['Price/day'][update_index] = int(input('Enter new price per day: '))
            if car_list['Price/day'][update_index] == 0 :
                print('You can not enter 0 for price/day, please try again.') 
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for Price.")
    
    print ('Car successfuly updated!')
    show_car_list(car_list)

    while(True): 
        update_more_car = input('do you want to update more car? (y/n): ').lower()
        if update_more_car == 'y': 
            staff_menu_update(car_list, cart_update, login_page)
            break
        elif update_more_car == 'n': 
            print('Car List Successfuly Updated. You will be directed to the Staff Menu')
            staff_menu(car_list, cart_update, login_page)
            break
        else: 
            print('Incorrect answer, please input y for yes, and n for no.')
            continue



def staff_menu_delete (car_list, cart_update, login_page): 
    while(True): 
        show_car_list(car_list)
        del_car = input("Which car you want to delete?  ").lower()
        if del_car.isdigit() : 
            del_car = int(del_car)

        if del_car in car_list["No"]:
            num_del = car_list['No'].index(del_car)
            car_list["No"].pop(num_del)
            car_list["Model"].pop(num_del)
            car_list["Type"].pop(num_del)
            car_list["Capacity"].pop(num_del)
            car_list["Stock"].pop(num_del)
            car_list["Price/day"].pop(num_del)
            new_numb = len(car_list['No'])
            car_list['No'] = [i+1 for i in range(new_numb)]

            print('Car successfuly deleted.')
            show_car_list(car_list)
            while(True):
                del_more = input('Do you want to delete another car? (y/n): ').lower()
                if del_more == 'y': 
                    break
                elif del_more == 'n': 
                     staff_menu(car_list, cart_update, login_page)
                else : 
                    print('Please enter the correct answer!')
                    continue
        
        elif del_car == 'delete all' or del_car == 'all' : 
            confirm_del_all = input('Are you sure want to delete all cars? (y/n): ').lower()
            if confirm_del_all == 'y' : 
                for key in car_list.keys():
                    car_list[key] = []
                print('All car deleted successfully!')
                show_car_list(car_list)
                break
            elif confirm_del_all == 'n': 
                print('Delete all car canceled')
                break
                
        else : 
            print('Car Not Found, Please try again.')
            continue

