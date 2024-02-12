a, b, c = input(), input(), input()
if len(a) > len(b): 
    a, b = b, a  
if len(b) > len(c): 
    b, c = c, b
if len(a) > len(b):
    a, b = b, a  
print(c)
print(a)