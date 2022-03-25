# ----------* CHALLENGE 77 *----------
# Change program 076 so that once the user has completed their list of names, display the
# full list and ask them to type in one of the names on the list. Display the position of that
# name in the list. Ask the user if they still want that person to come to the party. If they
# answer “no”, delete that entry from the list and display the list again.

guest_list = []

for invitation in range (1,4):
    guest = input("Enter the name of a guest: ")
    guest_list.append(guest)
print(guest_list)

wannna_add_names = True

while wannna_add_names == True:
    answer = input("Do you want to add another names? ")
    answer = answer.lower()
    if answer == "yes":
        guest = input("Enter the name of a guest: ")
        guest_list.append(guest)
        wannna_add_names = True
    elif answer == "no":
        wannna_add_names = False
    else:
        print("Enter a correct answer.")

print("You invited",len(guest_list),"guests.")
print(guest_list)

answer_name = True

while answer_name == True:
    guest = input("Enter the name of one of the guest on the list: ")
    if guest in guest_list:
        print("The index of this guest is",guest_list.index(guest))
        remove_name = input("Do you still want to invite this person to the party? ")
        remove_name = remove_name.lower()
        if remove_name == "no":
            guest_list.remove(guest)
            answer_name = False
        elif remove_name == "yes":
            answer_name = False
    else:
        print("Enter a correct name.")
        answer_name = True
print(guest_list)
