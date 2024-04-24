import stats

numbers = [1, 2, 3, 4, 5]
print(stats.mode(numbers))  # Output: 1 (or any other number, since they all appear once)

numbers = [1, 2, 2, 3, 3, 3]
print(stats.mode(numbers))  # Output: 3