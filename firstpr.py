

while True:
    n=int(input("Enter Number: "))

    if n%5==0:
        if n%10==0:
            print(f"{n} is multipal of 5 and 10 both.")
            
        else:
            print(f"{n} is multipal of five")
            
    elif n%7==0:
        if n%56==0:
            print(f"{n} is multipal of both 7 and 56.")
       
        else:
            print(f"{n} is multipal of 7.")
       
    else:
        print("It is Not multipal of any number that given")


    choice=input("Enter y for continue and n for exit: (y/n)").lower()
    if choice=="n":
        print("program is finish")
        break
