# Loop

people = ['John','Sara','Tim','Bob']
for person in people:
    print('Current Person: ', person)
    
# Iterate by seq Index
for i in range(len(people)):
    print('Current Person:', people[i])
 
# limit for loop   
for i in people[:2]:
    print(i)
    
#range
for i in range(0,10):
    print(i)
    
# While Loop

count = 0
while count < 7:
    print('Count: ', count)
    count += 1
    if count == 5:
        break