import array as arr  #array of numeric values are supported in Python by the array module


# Arrays are one of the simplest ds

numbers= arr.array('i', [1, 2,3,4,5])
#loop the array with while loop
i = 0

while i < len(numbers):
    print(numbers[i])
    i = i +1

# list type array

strings = ['a', 'b', 'c']
for x in strings:
    print (x)