import functions
import read
import write

print("---------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t WELCOME to Abc electronics ! ")
print("---------------------------------------------------------------------------------------------------------------------------------")
print("\n")


# File splitting
read.datastoredin_dictionary()

loop = True
while loop == True:

    # Display message 
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("1 - Sell the laptop to the customer")
    print("2 - Purchase laptop from manufacturer")
    print("3 - Exit system")
    print("\n")

    loop_checker = True # Input number  
    while loop_checker == True :
        try :
            user_input = int(input("Enter option from above: "))
            loop_checker = False
        except ValueError :
            print("Enter the number  ")

    if user_input == 1 :
        print("\n")
        name = input("Enter the customer's name: ")
        print("\n")
        address = input("Enter the customer's address: ") 
        print("\n")
        phone_number = input(" Enter the customer's phone_number: ")
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        
        quantity_list_for_users_purchase = []# k kineko vanera yeta basxa   
        more_quan_pur = True 

        while more_quan_pur == True:

            print("---------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t\t Laptop Name \t\t Company Name \t\t price \t\t Quantity \t\t CPU \t\t GPU")
            print("---------------------------------------------------------------------------------------------------------------------------------")

            read.tabledata_displaying()

            details_of_laptop = read.datastoredin_dictionary () 
            
            identification_of_laptop = functions.identification_of_laptop_validation(details_of_laptop) # lautau ko id mageko  

            quantity_of_chosen_laptop = details_of_laptop [identification_of_laptop] [3]  

            if int(details_of_laptop [identification_of_laptop] [3]) == 0: # stock 0 xa ki xaina check gareko 
                print("yo lautau ta sakkio ") 
                continue 
            else :
                quantity_bought_by_user = functions.laptops_bought_quantity() # quatity mageko ani validate gareko


                # Updating text file 

                details_of_laptop[identification_of_laptop] [3] = int(details_of_laptop[identification_of_laptop] [3]) - int(quantity_bought_by_user)

                write.stock_regeneration(details_of_laptop)



                # Getting purchased items

               

                name_of_the_product = details_of_laptop [identification_of_laptop] [0]  
                name_of_brand = details_of_laptop [identification_of_laptop] [1] 
                quantity_chosen_by_user = quantity_bought_by_user 
                price_per_laptop = details_of_laptop [identification_of_laptop] [2] .replace("$",'')
                overall_price = int(price_per_laptop)*int(quantity_chosen_by_user) 

                quantity_list_for_users_purchase.append ([name_of_the_product, name_of_brand, quantity_chosen_by_user, price_per_laptop, overall_price]) # 2d list ho (list vitra list)

                proceed_further_sales = input("Proceed sales to customer ? \nPress Y to continue selling OR press * ENTER * key to proceed to billing: ").upper() # variable name change ( aajhai bechne lai change )

                if proceed_further_sales == "Y" :
                    more_quan_pur = True 

                else :
                    write.generation_of_bill(quantity_list_for_users_purchase,name,address,phone_number)
                    more_quan_pur = False

    elif user_input == 2 :
        print("\n")
        name = input("Enter customer's name: ")
        print("\n")
        address = input("Enter customer's address: ")
        print("\n")
        phone_number = input("Enter customr's phone number: ")
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        quantity_list_for_users_purchase = [] 
        more_quan_pur = True 

        while more_quan_pur == True:
                # New function for printed items
            print("---------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t\t Laptop Name \t\t Company Name \t\t price \t\t Quantity \t\t CPU \t\t GPU")
            print("---------------------------------------------------------------------------------------------------------------------------------")

            read.tabledata_displaying()

            details_of_laptop = read.datastoredin_dictionary ()
            
            identification_of_laptop = functions.identification_of_laptop_validation(details_of_laptop) 

            quantity_of_selected_laptop = details_of_laptop [identification_of_laptop] [3] 

           
            
            quantity_bought_by_user = functions.laptops_bought_quantity() 

                # Updating text file 

            details_of_laptop[identification_of_laptop] [3] = int(details_of_laptop[identification_of_laptop] [3]) + int(quantity_bought_by_user)

            write.stock_regeneration(details_of_laptop)



                # Getting purchased items

                

            name_of_the_product = details_of_laptop [identification_of_laptop] [0] 
            name_of_brand = details_of_laptop [identification_of_laptop] [1] 
            quantity_chosen_by_user = quantity_bought_by_user 
            price_per_laptop = details_of_laptop [identification_of_laptop] [2] .replace("$",'')
            overall_price = int(price_per_laptop)*int(quantity_chosen_by_user)

            quantity_list_for_users_purchase.append ([name_of_the_product, name_of_brand, quantity_chosen_by_user, price_per_laptop, overall_price]) # 2d list ho (list vitra list)
            proceed_further_sales = input("Proceed sales to customer ? \nPress Y to continue selling OR press * ENTER * key to proceed to billing: ").upper()

            if proceed_further_sales == "Y" :
                more_quan_pur = True 

            else :
                write.purchased_generation_of_bill(quantity_list_for_users_purchase,name,phone_number)
                more_quan_pur = False


    elif user_input == 3 :
        loop = False
        print("exited system")
