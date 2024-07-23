
def identification_of_laptop_validation (laptops_detail):  

    identity_of_user = int(input("Enter the laptop id that you want to buy: "))
    print("\n")

    
    while identity_of_user <= 0 or identity_of_user > len(laptops_detail):
        print("Do provide a valid laptop id ")
        print("\n")
                
        identity_of_user = int(input("Enter the laptop id that you want to buy: "))
        print("\n")
    return identity_of_user

def quantity_of_laptop(quantity_of_chosen_laptop): 
    quantity_bought_by_user = int(input("The quantity you want to buy: ")) 
    while quantity_bought_by_user <= 0 or quantity_bought_by_user > int(quantity_of_chosen_laptop):
        print("The quantity you requested is not available right now")
        print("\n")

        quantity_bought_by_user = int(input("Enter the quantity you want to buy: "))
        print("\n")

    return quantity_bought_by_user

# for option 2 
def laptops_bought_quantity(): 
    quantity_bought_by_user = int(input("The quantity you want to buy: ")) 
    while quantity_bought_by_user <= 0:
        print("The quantity you requested is not available right now")
        print("\n")

        quantity_bought_by_user = int(input("Enter the quantity you want to buy: ")) 
        print("\n")

    return quantity_bought_by_user
