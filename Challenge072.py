# ----------* CHALLENGE 72 *----------
# Create a list of six school subjects. Ask the user which of these
# subjects they don’t like. Delete the subject they have chosen from the
# list before you display the list again.

subjects = ["history", "biology", "english", "literature", "maths", "philosophy"]

print(subjects)

delete = input("Which subject doesn't like it?: ")

subjects.remove(delete)

print(sorted(subjects))