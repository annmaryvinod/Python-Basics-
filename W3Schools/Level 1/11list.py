mylist = ["apple", "banana", "cherry"]


print(mylist)


# Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#Negative Indexing
#Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.


thislist = ["apple", "banana", "cherry"]


print(thislist[-1])     # Print the last item of the list



# Range of Indexes

  # Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
 

#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# Remove "banana":

thislist.remove("banana")
print(thislist)


thislist.remove("apple")
print(thislist)





# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



  newList = ["goat","sheep","kitten"]

  for y in newList:
        print(y)

