#working with files

#open()
#open('filename', mode='r')

opnfile = open('examplefile.txt', 'r') #r = read, this is default, don't need to specify
opnfile.read() #will return contents of file

print(opnfile.read())

#.read will iterate through the file
#so if you call it again, it will return no characters
#seek is used to reset

opnfile.seek(0)
print(opnfile.read())

opnfile.seek(0)

for lines in opnfile:
