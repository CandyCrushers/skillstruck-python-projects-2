answer = "y"
list = []
while answer == 'y':
    name = input("Give a name")
    answer = input("y or n")
    list.append(name)
    if answer == 'n':  
        print(list.sort())
    

