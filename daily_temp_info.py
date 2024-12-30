my_dict = {}
i=0

print("Welcome!")
while i!=3:
    i = int(input("Enter 1 To Insert Data,2 To Display Data,3 to Exit:"))
    if i == 1:
        choice=input("Enter Which Day You Want to Enter Temperature In:")
        if  choice=="Monday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        elif choice=="Tuesday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        elif choice=="Wednesday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        elif choice=="Thursday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        elif choice=="Friday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        elif choice=="Saturday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        elif choice=="Sunday":
            temp=int(input(f"Enter {choice} Temperature:"))
            my_dict[choice]=temp

        else:
            print("Invalid Day!")                
    elif i == 2:
        if my_dict:
            print("Displaying Data:")
            for day, temp in my_dict.items():
                print(f"{day}: {temp}°C")  
        else:
            print("No data to display.")






    