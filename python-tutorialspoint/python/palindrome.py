def is_palindrome(input_string):   
    str_to_list = list(input_string)
    len_list = len(str_to_list)    
    reverse_string_list = []    
    while len_list > 0:        
        grep_last_list_element = str_to_list[-1]
        remove_last_list_element = str_to_list.pop()
        reverse_string_list.append(grep_last_list_element)
        len_list = len_list -1             
        reverse_string = ""
    reverse_string = reverse_string.join(x for x in reverse_string_list)  
    if input_string == reverse_string:
        return True
    else: 
        return False
        
result = is_palindrome("racecar")

print(result)