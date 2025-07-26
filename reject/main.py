def reject(array, predicate):
    return [item for item in array if not predicate(item)]

numbers = [1, 2, 3, 4, 5, 6]

filtered_numbers = reject(numbers, lambda x: x % 2 == 0)

# 1, 3, 5
print(f"reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) => {filtered_numbers}") # Salida: [1, 3, 5]

words = ["apple", "banana", "cherry", "date"]

filtered_words = reject(words, lambda s: 'a' in s)
print(f"reject(['apple', 'banana', 'cherry', 'date'], lambda s: 'a' in s) => {reject(words, lambda s: 'a' in s)}") # Salida: ['cherry']

another_list = [0, 1, 2, 3, 4, 5, 6, 7]

filtered_another_list = reject(another_list, lambda x: x > 3)
print(f"reject([0, 1, 2, 3, 4, 5, 6, 7], lambda x: x > 3) => {filtered_another_list}")