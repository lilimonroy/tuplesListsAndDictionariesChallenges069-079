# ----------* CHALLENGE 62 *----------
# Create a tuple containing the names of five countries and display the whole tuple. Ask
# the user to enter one of the countries that have been shown to them and then display
# the index number (i.e. position in the list) of that item in the tuple.

tuple_countries = ("Mexico", "Japan", "Ireland", "Germany", "Egypt")

print(tuple_countries)

country = input("Enter the country: ")

print(tuple_countries.index(country))
