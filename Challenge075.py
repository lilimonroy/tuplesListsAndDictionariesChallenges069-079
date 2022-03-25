# ----------* CHALLENGE 75 *----------
# Create a list of four three-digit numbers. Display the list to the user, showing each item from 
# the list on a separate line. Ask the user to enter a three-digit number. If the number they
# have typed in matches one in the list, display the position of that number in the list,
# otherwise display the message “That is not in the list”.

number_list = [123, 234, 569, 874]

# Read the value of the index in the list. 
# Uses the items in the list in a for loop, useful if you want to print the items in a list on separate lines.
for iteration in number_list: 
    print(iteration)

new_number = int(input("Enter a new number: "))

if new_number in number_list:
    print(number_list.index(new_number))
else:
    print("That is not in the list")