print("All perfect numbers below 1 million are: \n")
for num in range(1, 1000000):
    sum_of_divisors = 0
    
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_of_divisors += divisor
    
    if sum_of_divisors == num:
        print(num)