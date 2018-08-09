from math import sqrt
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':


print("Starts with D:")
# r = []  # TODO
# def the_letter():
#     first_letter = human.name[0]
#     if first_letter == 'D':
#         return human

# r = [human for human in humans lambda x: the_letter ]
# for human in humans:
#     first_letter = human.name[0]
#     if first_letter == 'D':
#         r.append(human)

r = [human for human in humans if human.name[0] == 'D']
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")

r = [human for human in humans if human.name[-1] == 'e']
print(r)


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
# r = []  # TODO
# for human in humans:
#     a_letter = human.name[0]
#     for i in ['C', 'D', 'E', 'F', 'G']:
#         if i == a_letter:
#             r.append(human)
r = [human for human in humans if (human.name[0] >= "C" and human.name[0] <= "G")]
print(r)


# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [human.age + 10 for human in humans]
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [str(human.name) + '-' + str(human.age) for human in humans]  # TODO
for human in humans:
    hyphenated_name = human.name + '-' + str(human.age)
    r.append(hyphenated_name)
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = [(human.name, human.age) for human in humans if (human.age in range(26, 33))]
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = [[human.name.upper(), human.age + 5] for human in humans]  # TODO

print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = [sqrt(human.age) for human in humans]  # TODO
print(r)