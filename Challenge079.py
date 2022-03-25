# ----------* CHALLENGE 79 *----------
# Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add
# it to the end of the nums list and display the list. Once they have entered three numbers, ask them if 
# they still want the last number they entered saved. If they say “no”, remove the last item from the list.
# Display the list of numbers.

nums = []

for times in range(1,4):
    number = int(input("Enter a number: "))
    nums.append(number)

answer = input("Do you still want to save the last number entered? ")
answer = answer.lower()

if answer == "no":
    nums.pop(len(nums)-1)
    print(nums)
elif answer == "yes":
    print(nums)
else:
    print("That is no valid answer.")

