#01-Input User List Separated by Spaces
inputList = input("Enter your List and separate it by space: ")

  
#02-Converting input string to a list of integers  
inputList = inputList.split()  
inputList = [int(i) for i in inputList]  

#03-Count 4 in a given list and print it
print("The occurance of 4 is", inputList.count(4))