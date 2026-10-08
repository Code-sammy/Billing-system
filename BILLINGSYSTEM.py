print("WELCOME TO SAMMY'S SHOP")
print("WE PROVIDE DIFFERENT KINDS OF CLOTHES AS LISTED")

print("JACKET 1 PIECE 40 DOLLARS")
ja=40                          
print("COAT 1 PIECE 50 DOLLARS")
co=50
print("Boots 1 PAIR 20 DOLLARS")
bo=20
print("PANT 1 PIECE  30 DOLLARS ")
pa=30

a1=str(input("please enter your choice of clothing one at a time: ")).lower()
b1=int(input(f"how many piece of {a1} do u want to buy: "))
cost=0
def clothes():
    global cost
    if a1=="jacket":
        cost=cost+ja*b1
    elif a1=="coat":
        cost=cost+co*b1
    elif a1=="boots":
        cost=cost+bo*b1
    elif a1=="pant":
        cost=cost+pa*b1
    else:
        print("invalid item")
clothes()
choice=str(input("Do u want more items (y/n) ")).lower()
while choice=="y":
    a1=str(input("please enter clothes of your like: ")).lower()
    b1=int(input(f"enter the amount of {a1} you would like: "))
    choice=str(input("Do u want more items (y/n): ")) 
    clothes()
print(f"your total is {cost}")
print("THANK YOU FOR VISITING!!!!")





    
