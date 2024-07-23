def datastoredin_dictionary ():  

    """ creating a list inside dictionary """
    
    file = open("laptops.txt","r")
    details_of_laptop = {}  
    identification_of_laptop = 1
    for line in file :
        line = line.replace("\n","")
        details_of_laptop.update({identification_of_laptop: line.split(",")}) # {1:[razer,...],2:[xps,...],3:[sdasfd]}
        identification_of_laptop = identification_of_laptop + 1 
    file.close()
    return details_of_laptop

def tabledata_displaying ():  
    file = open("laptops.txt","r")
    a = 1
    for line in file :
        print(a, "\t\t" + line.replace("," , "\t\t"))
        a = a + 1
        print("---------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")
