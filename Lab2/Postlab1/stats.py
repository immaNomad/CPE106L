#Mean Function
def mean(numbers):
  return sum(numbers) / len(numbers)

#Mode Function
def mode(numbers):
  frequency = {}
  for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
  max_freq = max(frequency.values())
  modes = [num for num, freq in frequency.items() if freq == max_freq]
  return modes[0] if len(modes) == 1 else modes

#Median Function
def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    
# test case
numbers = [5, 10, 15, 15, 25]
print("Median:", median(numbers))
print("Mode:", mode(numbers))
print("Mean:", mean(numbers))
