list1=[1,2,3,4,5,6,"a","b"]
#length of the list
print(len(list1))
#accessitem
print(list1[3]) #in python indexing always starts from 0
#python also have the concept of negative indexing which starts from last index of the list
print(list1[-1])
#we can occur the charcters in list from one speficie index to the next index or in a particular range
print(list1[2:5])
print(list1[:4])
print(list1[2:])
#changing list items
list1[1]="apple"
print(list1)
#changing the range of item in list
list1[2:4]=["pink" , "blue" , "black"]
print(list1)
#if you insert more items then the range then the remaining item will be stored in the list in order only and existing elements will shift accordingly
list1[1:2]=["H" , "j" , "k"]
print(list1)
list1[1:2]=["q"]
print(list1)
#to insert new item at specific  postion without replacing old one
list1.insert(2,"app")
print(list1)
#to add an item to the end of the list we will use append method
list1.append("orange")
print(list1)
#to remove specified item
list1.remove(1)
#to remove from specific index
list1.pop(1)
#del keyword is also used to remove specific index element
del list1[1]
#clear method empties the list
list1.clear()
print(list1)
