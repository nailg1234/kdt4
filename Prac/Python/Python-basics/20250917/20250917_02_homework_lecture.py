squares = [x ** 2 for x in range(11)]
print(squares)

new_list = [i for i in range(1, 50) if i % 3 == 0]
print(new_list)

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]

new_list = [fruit for fruit in fruits if len(fruit) >= 5]
print(new_list)
