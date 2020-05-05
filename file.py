
# Read Files

# # find the file and store it in a variable

# inputFile = open('inputFile.txt', "r" ); 

# # print the entire file to the clg
# print(inputFile.read()); 

# # Always close the file once it is done
# inputFile.close(); 

# f = open("inputFile.txt", "r")

# count = 0; 
# for line in f:
#     print(str(count) + line)
#     count = count + 1
# f.close()

f = open("inputFile.txt", "r")
count = 0 
for line in f: 
    line_split = line.split()
    if line_split[2] == "P":
        print("You Passed => " + line)
    elif line_split[2] == "F":
        print("You failed => " + line)
f.close()