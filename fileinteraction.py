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
    print(lines, end="")  #end="" specifies not to print new line after each object
    
    
opnfile.close() #close file once finished
opnfile.name

#to create a copy of a file
opnfilebase = open('opnfile.txt', 'r') #open the original file first and assign to name like file_base

#create a new file which will be written to
newopnfile = open('newopnfile.txt', 'w') #w - truncates any existing file, contents will be overwritten
newopnfile.write(opnfilebase.read()) #takes opnfile.txt and reads it into new object newopnfile, then returns number of chars
newopnfile.close() #close out the open file

newopnfile = open(newopnfile.name, 'r+') #r+ lets read and write to new file
newopnfile.read()
newopnfile.seek(0)

newopnfile.write("Cigarette Smoking Man\n") #will write to seek position, ovewriting what's already there by number of characters passed in
newopnfile.seek(0)
newopnfile.read()
