def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return 1 #non prime
    return 0 #prime

# flag = check_prime(n)
while True:
    n=int(input("Please enter a number: "))
    flag = check_prime(n)
    if flag==1 or n==0 or n==1:
        print(f"{n} is a not a prime number")
        continue
    else:
        print(f"{n} is a prime number")
        break
    
