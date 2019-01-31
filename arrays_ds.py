import array as arr  #array of numeric values are supported in Python by the array module

sortd= arr.array('i', [1, 2,3,4,5])
unsorted = arr.array('i', [4, 8, 2,5,7,1,3,6])

count = 0



# #List example to show difference
# strings = ['a', 'b', 'c']  # # Simple list type array
# for x in strings:
#     print (x)

#  #print with while loop
def printW(count):
    while count < len(sortd):
        print(sortd[count])
        count = count +1


# Print items in arrays with forloop
def printFor():
    for item in sortd:
        print (item)
# printFor()
#  #-------------------------------------

#  #reverse items in array using reverse iteration
def reverse():
    pass

# # #append items to array
# def add():
#     pass


# # #prepend items to array
# def prepend():
#     pass

# # #delete items from array
# def remove():
#     pass


