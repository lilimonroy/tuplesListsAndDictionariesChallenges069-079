# ----------* CHALLENGE 62 *----------
# Add to program 069 to ask the user to enter a number and display the country in that position.
tuple_countries = ("Mexico", "Japan", "Ireland", "Germany", "Egypt")

print(tuple_countries)

country = input("Enter the country: ")

print(tuple_countries.index(country))

index_country = int(input("Enter the index: "))

print(tuple_countries[index_country])