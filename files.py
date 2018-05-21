# Open a file

fo = open('text.txt', 'w')

# Get some info
print('Name: ', fo.name)
print('Is closed: ', fo.closed)
print('Opening Mode: ', fo.mode)
# Write to file
fo.write('I love Python')
fo.write(' and Javascript')
# Close file
fo.close()

# Open to append
fo = open('text.txt', 'a')
fo.write(' I also like PHP')
fo.close()

# Read from file
fo = open('text.txt', 'r+')
text = fo.read()
print(text)

# Create a file
fo = open('text2.txt', 'w+')
fo.write('This is my new file')
fo.close()