# Python program to find the factorial of a number using recursion.
#  Note: Input should be taken from the terminal.


while True:
    n=int(input("Enter Number to find factorial: "))

    def fact(n):
        if n==1:
            return 1
        else:
            return ((fact(n-1)* n))
        

    print(fact(n))

    choice=input("yes for continue and no for stop(y/n):").lower()
    if choice=="n":
        print("stop")
        break

