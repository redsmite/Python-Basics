# Conditionals

x = 4

# Basic If
if x < 6:
    print('This is true')
    print('Indent is important')
    
# If-Else
if x < 6:
    print ('This is true')
else:
    print('This is false')
    
# Elif
color ='red'

if color =='red':
    print('Color is red')
elif color == 'blue':
    print('Color os not red or blue')
else:
    print('Color is not red or blue')
    
# nest if
if color == 'red':
    if x < 10:
        print('Color is red and x is less than 10')
        
# Logical Operators
if color == 'red' and x < 10
    print('Color is red and x is less than 10')
