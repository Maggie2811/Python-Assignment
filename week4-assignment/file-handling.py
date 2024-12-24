file = open("myData.txt", "r") 

print(file.read()) # Read the entire content of the file
           
# write a new file
newfile = open("filename.txt", "w")
newfile.write("We add the content of the file")