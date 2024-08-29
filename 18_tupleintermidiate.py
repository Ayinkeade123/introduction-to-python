def squared_tuple_number (numbers):
    new_tuple = tuple (x ** 2 for x in numbers)
    return new_tuple

numbers = (1, 2, 3, 4, 10)
new_numbers = squared_tuple_number (numbers)
print (numbers)
print (new_numbers)

numbers = (1, 2, 3, 4, 10)
new_numbers = []

for x in numbers:
    new_numbers.append (x ** 2)

new_numbers = tuple(new_numbers)
print (numbers)   
print (new_numbers)
    