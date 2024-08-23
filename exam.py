#create an account

full_name=input("your full name: ")

card=int(input("Enter your card number: "))

#deposit
deposit=int(input("how much to deposit: "))

if deposit > 0:
    print("seccesfuly deposited" + deposit)

elif deposit <0:
    print("enter a valid number")

else: 
    deposit=int(input("how much to deposit: "))  


#widthdraw

widthdraw=input( " would you like to widthdraw money from " + card + "? ")
if widthdraw.lower == "yes":
    widthdraw2=int(input("how much would you like to widthdraw? "))

print(widthdraw2 + "has been succesfuly widthrown from your card")

#exit

exit=input("would you like to exit from the program? ")
if exit.lower =="yes":
    quit()

