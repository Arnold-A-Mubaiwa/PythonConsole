# print("Hello World")
# try :
#     num1 = 5
#     num2 = 0
#     answer= num1/num2
# except ZeroDivisionError:
#     print("You should not devide by 0")
# Files

file = open("file.txt", 'r')
# for line in file:
#     print(line, end='')
print(file.read(16))
print(file.read(4))
file.close()

n_file = open("newfile.txt", "w")

n_file.write("This has been written to a file")
n_file.close()

with open("newfile.txt") as f:
    print(f.read())