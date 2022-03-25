# ----------* CHALLENGE 76 *----------
# Ask the user to enter the names of three people they want to 
# invite to a party and store them in a list. After they have entered 
# all three names, ask them if they want to add another. If they do, 
# allow them to add more names until they answer “no”. When
# they answer “no”, display how many people they have invited to the party.

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