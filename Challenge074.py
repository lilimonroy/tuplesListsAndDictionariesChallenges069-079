# ----------* CHALLENGE 74 *----------
# Enter a list of ten colours. Ask the user for a starting number between 0 and 4
# and an end number between 5 and 9. Display the list for those colours 
# between the start and end numbers the user input.

list_colours = ["red", "blue", "green", "yellow", "orange", "purple", "brown", "cyan", "pink", "burgundy", "olive"]

first_index = int(input("Enter a number between 0 and 4: "))
last_index = int(input("Enter a number between 5 and 9: "))

print(list_colours[first_index:last_index+1])