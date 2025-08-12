'''
This is Module Docstring

'''


TAX = 0.1

def tax_calculator():
    '''
    The main function for calculating TAX_TO_PAY.

    '''
    
    salary = int(input("What is your salary?: "))
    tax_to_pay = salary * TAX
    return tax_to_pay
    
print(tax_calculator())
print(TAX)
