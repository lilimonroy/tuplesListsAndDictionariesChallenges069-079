# ----------* CHALLENGE 73 *----------
# Ask the user to enter four of their favourite foods and store them in a dictionary so that they are
# indexed with numbers starting from 1. Display the dictionary in full, showing the index number
# and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining
# data and display the dictionary.

food_dictionary = {}
for number in range (1,5):
    food = input("Enter your favorite food: ")
    food_dictionary[number] = food
print(food_dictionary)

#Remember that here convert the 'key' to 'int' because we assigned the 'key' as a 'int' in the 'for' loop.
foodIndex_out = int(input("Which food do you want to get rid of? [Write the number] ")) 

if foodIndex_out in food_dictionary:
    del food_dictionary[foodIndex_out]
else:
    print("This food is not in the menu.")

print(sorted(food_dictionary.values()))
