# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
total_class1 = Counter(class1)
print(f"Total de itens na Classe 1 =: {total_class1}")

total_class2 = Counter(class2)
print(f"Total de itens na Classe 2 =: {total_class2}")

# TODO: How many students in class 1 named James?
print(total_class1["James"])

# TODO: How many students are in class 1?
print(sum(total_class1.values()), "students in class1")

# TODO: Combine the two classes
total_class1.update(class2)
print(sum(total_class1.values()), "students in class1")

# TODO: What's the most common name in the two classes?
print(total_class1.most_common(3))

# TODO: Separate the classes again
total_class1.subtract(class2)
print(total_class1.most_common(1))

# TODO: What's common between the two classes?
print(total_class1 & total_class2)
