import array as arr  #array of numeric values are supported in Python by the array module

sortedList= arr.array('i', [1, 2,3,4,5])
unsorted = arr.array('i', [4, 8, 2,5,7,1,3,6])

count = 0



# #List example to show difference
## strings = ['a', 'b', 'c']  # # Simple list type array
## for x in strings:
##     print (x)
#
##  #print with while loop
#def printW(count):
#    while count < len(sortedList):
#        print(sortedList[count])
#        count = count +1
#
#
## Print items in arrays with forloop
#def printFor():
#    for item in sortedList:
#        print (item)
## printFor()
##  #-------------------------------------
#    
##    
#def reversefn():
#    #   #reverse items in array using reverse iteration
#    
#    sortedList.reverse()
#    
#    
#    #   #Reversing a list in-place with the list.reverse() method
#    for i in sortedList:
#        print("Reverse() iter :", i )
#        
#    print("...\n")
#    
#    #   #Using the “[::-1]” list slicing trick to create a reversed copy
#    
#    sortedList[::-1]
#    for x in sortedList:
#        print("Reverse [::-1] slicing :", x )
#        
#    print("...\n")
#    
#    #   #Creating a reverse iterator with the reversed() built-in function
#    
#    for xy in reversed(unsorted):
#        print("reversed(): ", xy)
#        
#    print("...\n")
#    
#reversefn()


# # #append items to array
def add1(x, sortedList):
     newList = arr.array('i',[x])
     sortedList +=  newList
     for y in sortedList: 
         print(y, end=" "),

#add1(10, sortedList)

# ##add to list with built in methods

# #append takes only one arguement
def appendx(x):
    sortedList.append(x)
    print(sortedList)
    
#appendx(13)

# #add items to list using extend([])
def extendY(*args):
    sortedList.extend([*args])
    for y in sortedList: 
        print( y, end=" ")
extendY(10,7,6,8,9)



#add at x or y location in list

def add_at:
    pass

# # #prepend items to array
# def prepend():
#     pass

# # #delete items from array
# def remove():
#     pass


