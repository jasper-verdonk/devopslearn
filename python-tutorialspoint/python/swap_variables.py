def swap_variables_integers(a, b):
    a = a + b
    b = a - b # b = (a + b) - b = a
    a = a - b # a = (a + b) - a = b
    
   
    
    return a, b
a = 5
b = 10
print(f"The value of a equals %s and the value of b equals %s" % (a, b))
print(f"The value after swapping: a equals %s and the value of b equals %s" % swap_variables_integers(5, 10))

def swap_string_text(string1, string2):
    
    string1, string2 = string2, string1
    # multiple assignment
    return string1, string2

text_1 = "Hello"
text_2 = "World!"

print(f"The content of text_1 equals %s and the content of text_2 equals %s" % (text_1, text_2))
print(f"The content after swapping: text_1 equals %s and the context of text_2 equals %s" % swap_string_text(text_1, text_2))