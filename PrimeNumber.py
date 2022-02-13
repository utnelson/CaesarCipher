#Write your code below this line 👇
def prime_checker(number):
    # Variable triggert sobald 1x das if Statement wahr ist
    is_prime = True
    for item in range(2, number):
        if number % item == 0:
            is_prime = False
    if is_prime:
        print("It's a prime")
    else:
        print("Its not a prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



