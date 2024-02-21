import random

# Return a random float number between certain interval

random_float = random.uniform(1, 10)
print(random_float)

# Returns a random int number between a certain interval

random_int = random.randint(1, 100)
print(random_int)

# Neat trick to take random words from a given string

long_string = "This is a very long string that should be used to test the random package in Python"
l = long_string.split(" ")
print(random.choice(l))

# You can create a list with values pickup randomly from a list of predefined value

predefined_list = ['Red', 'Black', 'Green']
random_list = random.choice(predefined_list)  # This will create a list of 20 elements randomly selected form the list of predefined values
print(random_list)

# You can specify weights on the list as well. Red:18 out of 38, Green: 2 out of 38, Black: 18 out of 38

predefined_list1 = ['Red', 'Black', 'Green']
random_list1 = random.choices(predefined_list1, weights=[18, 18, 2], k=20)  # This will create a list of 20 elements randomly selected form the list of predefined values
print(random_list1)

# Shuffle a deck of cards
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

# Generates a random int number in a certain interval
k = random.randint(1, 99)
print(k)
