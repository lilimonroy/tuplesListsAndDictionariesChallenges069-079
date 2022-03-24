#----------* CHALLENGE 71 *----------
# Create a list of two sports. Ask the user what their favourite sport is and
# add this to the end of the list. Sort the list and display it.

list_sports = ["fencing", "archery"]

list_sports.append(input("Enter your favorite sport: "))

print(sorted(list_sports))

