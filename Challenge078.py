# ----------* CHALLENGE 78 *----------
# Create a list containing the titles of four TV programmes and display them on separate lines. Ask the
# user to enter another show and a position they want it inserted into the list. Display the list again,
# showing all five TV programmes in their new positions.


from numpy import append


show_list = ["Game Of Thrones", "Vikings", "The Great", "Love, Death and Robots"]

for each_show in show_list:
    print(each_show)

new_show = input("Enter a new TV Show: ")
index_new_show = int(input("Enter the position you want it inserted into the list: "))

show_list.insert(index_new_show-1, new_show)

for each_show in show_list:
    print(each_show)


