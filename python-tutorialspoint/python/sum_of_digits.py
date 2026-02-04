def sum_of_digits(n):  
    n = abs(n)            #convert into an integer (>0)
    total = 0    
    while n > 0:
        total += n % 10   #taking modulo of 10. This is exctract the last digit of the integer. 
        n = n // 10       #remove the last digit of the integer.               
    return total
        
result = sum_of_digits(123)
# Printing the result
print(result)