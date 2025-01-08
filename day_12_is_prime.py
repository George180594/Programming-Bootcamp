def is_prime(num):
    numbers=[]
    for n in range(1,num+1):
        if num%n==0:
            numbers.append(n)
    if len(numbers)>2:
        print('not prime')
        return False
    elif len(numbers)<=2:
        print('prime')
        return True
is_prime(75)
is_prime(73)

            