# List Comprehension

a = [2,3,4,5]

res = [val**2 for val in a]

print(res)


# Example -->  2

data = [1,2,3,4,5,6,7,8,9,10]
new_data = [x for x in data if x % 2 == 0]
print(new_data) # Even numbers


# Example : 3 --> Print odd numbers for the above data by using list comprehension.

odd_data = [y for y in data if y % 2 != 0]
print(odd_data) # odd numbers

# Example : 4 --> Print 1 to 100 natural numbers by using list comprehension.

natural_num = [z for z in range(101)]
print(natural_num)

# Example : 5 -->  Convert a list of strings to uppercase
words = ["hello", "world", "python"]
upperCase_data = [word.upper() for word in words]
print(upperCase_data)

# Example : 6 --> Find the length of each word in a list
words = ["apple", "banana", "cherry"]
word_length = [len(word) for word in words]
print(word_length)


# Example : 7 --> Reverse each word in a list
words = ["python", "list", "comprehension"]
reversed_words = [i[::-1] for i in words]
print(reversed_words)

# Example : 8 --> Generate a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
dictionary = {keys[i] : values[i] for i in range(len(keys))}
print(dictionary)