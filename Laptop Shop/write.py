import datetime

def stock_regeneration(details_of_laptop): 

    file = open ("laptops.txt","w")

    for values in details_of_laptop.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")

    file.close 

def generation_of_bill(quantity_list_for_users_purchase,name,address,phone_number): 

    total = 0 
    shipping_charge = 500
    for i in quantity_list_for_users_purchase :
        total += int(i[4])
    grand_total = total + shipping_charge 


    print("\n")
    print("\t\t\t\t SHOP BILL ")
    print("\n")
    print("\t\t Kirtipur, Kathmandu | 9841852012")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("laptop details are: ")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("name of customer: "+str(name))
    #print("address: "+str(address))
    print("contact number: "+str(phone_number))
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("purchase details are: ")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("name of product \t\t total qantity \t\t price per product \t\t\t total")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    for i in quantity_list_for_users_purchase :
        print(i[0],"\t\t\t",i[1], "\t\t\t", i[2], "\t\t\t","$", i[3], "\t\t\t", "$", i[4])
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("your total amount is: ", total) 
    print("your shipping cost is: ", shipping_charge)
    print("grand total: "+str(grand_total))
    print("Shipping charge has been added in grand  total")



    file = open (str(name)+str(phone_number)+"txt","w") 
    file.write("\n")
    file.write("\t\t\t\t shop bill \n")
    file.write("\n")
    file.write("\t\t Kirtipur,Kathmandu \n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("lapotp details are: \n")
    file.write("name of customer: "+str(name)+"\n")
    #file.write("address: "+str(address)+"\n")
    file.write("contact num"+str(phone_number)+ "\n" )
    file.write("\n")
    file.write("purchase detail are : \n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("name of product \t\t overall quantity \t\t price per product \t overall price \n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    for i in quantity_list_for_users_purchase:
        file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+"$"+str(i[4]))
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("\n")
    file.write("your shipping cost is: "+str(shipping_charge)+"\n")
    file.write("\n")
    file.write("grand total: $"+str (grand_total)+"\n")
    file.write("\n")
    file.write("*** shipping charge has been added in grand total ***"+"\n")
    file.write("\n")
    file.close()

   

def purchased_generation_of_bill(quantity_list_for_users_purchase,name,phone_number): 

    total = 0 
    vat = 0.13
    for i in quantity_list_for_users_purchase :
        total += int(i[4])
    vat_amount = 0.13* total
    grand_total = total + vat_amount



    print("\n")
    print("\t\t\t\t SHOP BILL ")
    print("\n")
    print("\t\t Kirtipur,Kathmandu | 9841852012")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("laptop details are: ")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("name of customer: "+str(name))
    #print("address: "+str(address))
    print("contact number: "+str(phone_number))
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("purchase details are: ")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("name of product \t\t overall quantity \t\t price per product \t\t\t overall price")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    for i in quantity_list_for_users_purchase :
        print(i[0],"\t\t\t",i[1], "\t\t\t", i[2], "\t\t\t","$", i[3], "\t\t\t", "$", i[4])
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("your total amount is: ", total) 
    print("your vat amount is: ", vat_amount) 
    print("grand total: "+str(grand_total))
    print("Shipping charge has been added in grand total")




    file = open (str(name)+str(phone_number)+"txt","w") 
    file.write("\n")
    file.write("\t\t\t\t shop bill \n")
    file.write("\n")
    file.write("\t\t Kirtipur \n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("lapotp details are: \n")
    file.write("name of customer: "+str(name)+"\n")
    #file.write("address: "+str(address)+"\n")
    file.write("contact num"+str(phone_number)+ "\n" )
    file.write("\n")
    file.write("purchase detail are : \n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("name of product \t\t overall quantity \t\t  price per product \t overall price \n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    for i in quantity_list_for_users_purchase:
        file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+"$"+str(i[4])+"\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("\n")
    file.write("your vat amount is: "+str(vat_amount)+"\n")
    file.write("\n")
    file.write("grand total: $"+str (grand_total)+"\n")
    file.write("\n")
    file.write("\n")
    file.close()

    
