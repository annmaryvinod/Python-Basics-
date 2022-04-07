# Since strings are arrays, we can loop through the characters in a string, with a for loop.


for x in "janmashadabthi" :
    print (x)


# The len() function returns the length of a string:

a = "Hippopottamus"    

print (len(a))




# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"

print ("best" in txt)





# Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


  # To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)